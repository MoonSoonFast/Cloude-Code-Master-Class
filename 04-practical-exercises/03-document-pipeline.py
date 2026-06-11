"""
Exercise 3: Document Processing Pipeline
Goal: Build the foundation of a real business — an AI document processor
      with structured outputs, streaming, and batch processing.

This is directly applicable to legal, finance, insurance, or any document-heavy industry.

pip install anthropic
export ANTHROPIC_API_KEY=your_key_here
"""

import anthropic
import json
import base64
from pathlib import Path

client = anthropic.Anthropic()

# ============================================================
# Structured Output: Extract data from any document
# ============================================================

CONTRACT_SCHEMA = {
    "name": "contract_analysis",
    "schema": {
        "type": "object",
        "properties": {
            "document_type": {
                "type": "string",
                "enum": ["NDA", "Service Agreement", "Employment Contract", "Lease", "Purchase Agreement", "Other"]
            },
            "parties": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "role": {"type": "string"}
                    },
                    "required": ["name", "role"]
                }
            },
            "effective_date": {"type": "string", "description": "ISO date format or null"},
            "expiration_date": {"type": "string", "description": "ISO date format or null"},
            "key_obligations": {
                "type": "array",
                "items": {"type": "string"}
            },
            "unusual_clauses": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "clause": {"type": "string"},
                        "risk_level": {"type": "string", "enum": ["low", "medium", "high"]},
                        "explanation": {"type": "string"}
                    },
                    "required": ["clause", "risk_level", "explanation"]
                }
            },
            "overall_risk_score": {
                "type": "integer",
                "minimum": 1,
                "maximum": 10,
                "description": "1 = very low risk, 10 = very high risk"
            },
            "recommendation": {
                "type": "string",
                "enum": ["approve", "approve_with_changes", "reject", "needs_legal_review"]
            },
            "summary": {"type": "string"}
        },
        "required": ["document_type", "parties", "key_obligations", "unusual_clauses", "overall_risk_score", "recommendation", "summary"]
    }
}


def analyze_contract(contract_text: str) -> dict:
    """
    Extract structured data from a contract.
    Returns guaranteed-valid JSON matching CONTRACT_SCHEMA.
    """
    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=4096,
        thinking={"type": "adaptive"},
        output_config={
            "format": {
                "type": "json_schema",
                "json_schema": CONTRACT_SCHEMA
            }
        },
        system="""You are an expert contract analyst. Extract all relevant information
        from the contract and assess risks carefully. Be specific about unusual clauses —
        anything that deviates from standard commercial terms should be flagged.""",
        messages=[{
            "role": "user",
            "content": f"Analyze this contract and extract all relevant information:\n\n{contract_text}"
        }]
    )

    return json.loads(response.content[0].text)


# ============================================================
# Streaming: Show progress for long documents
# ============================================================

def summarize_document_streaming(document_text: str):
    """
    Stream output for better UX on long documents.
    This is what you'd use in a web app — users see output immediately.
    """
    print("Analyzing document", end="", flush=True)

    with client.messages.stream(
        model="claude-opus-4-8",
        max_tokens=2048,
        system="You are an expert business document analyst. Provide clear, structured summaries.",
        messages=[{
            "role": "user",
            "content": f"Provide a comprehensive analysis of this document:\n\n{document_text}"
        }]
    ) as stream:
        print(" → streaming response:\n")
        for text_chunk in stream.text_stream:
            print(text_chunk, end="", flush=True)

        final = stream.get_final_message()
        print(f"\n\n[Total: {final.usage.input_tokens} in / {final.usage.output_tokens} out tokens]")


# ============================================================
# Batch Processing: Process many documents at low cost
# ============================================================

def create_batch_processing_job(documents: list[dict]) -> str:
    """
    Submit 100+ documents for async processing at 50% cost reduction.
    Returns batch_id to check later.
    """
    requests = []
    for i, doc in enumerate(documents):
        requests.append({
            "custom_id": f"doc_{doc['id']}",
            "params": {
                "model": "claude-opus-4-8",
                "max_tokens": 2048,
                "output_config": {
                    "format": {
                        "type": "json_schema",
                        "json_schema": CONTRACT_SCHEMA
                    }
                },
                "system": "You are a contract analyst. Extract all relevant information from contracts.",
                "messages": [{
                    "role": "user",
                    "content": f"Analyze this contract:\n\n{doc['text']}"
                }]
            }
        })

    batch = client.messages.batches.create(requests=requests)

    print(f"Batch created: {batch.id}")
    print(f"Processing {len(requests)} documents at 50% reduced cost")
    print(f"Check status: client.messages.batches.retrieve('{batch.id}')")
    print(f"Estimated completion: within 24 hours (usually much faster)")

    return batch.id


def retrieve_batch_results(batch_id: str) -> list[dict]:
    """Check and retrieve completed batch results."""
    batch = client.messages.batches.retrieve(batch_id)

    if batch.processing_status != "ended":
        print(f"Batch not complete. Status: {batch.processing_status}")
        print(f"Counts: {batch.request_counts}")
        return []

    results = []
    for result in client.messages.batches.results(batch_id):
        if result.result.type == "succeeded":
            doc_data = json.loads(result.result.message.content[0].text)
            results.append({
                "id": result.custom_id,
                "data": doc_data
            })
        else:
            print(f"Failed: {result.custom_id} — {result.result.error}")

    return results


# ============================================================
# Demonstration
# ============================================================

SAMPLE_CONTRACT = """
SERVICE AGREEMENT

This Service Agreement ("Agreement") is entered into as of January 1, 2025, between:
- Acme Corp ("Client"), a Delaware corporation
- TechVendor LLC ("Vendor"), a California LLC

SERVICES: Vendor will provide software development services including API integration,
data processing pipelines, and ongoing maintenance.

PAYMENT: Client agrees to pay $25,000/month. All invoices due within 7 days of receipt
(industry standard is 30 days). Late payment incurs 5% daily interest.

INTELLECTUAL PROPERTY: All work product, including pre-existing Vendor IP incorporated
into deliverables, shall become sole property of Client upon payment.

LIMITATION OF LIABILITY: Vendor's liability shall not exceed $1,000 total for any claims
arising under this agreement, regardless of type of damages.

TERM: 24 months, auto-renewing. Either party may terminate with 90 days notice, except
Client must pay 12 months of fees upon any termination.

NON-COMPETE: Vendor agrees not to work with any Client competitors (defined as any company
in the technology industry) for 5 years after agreement ends.
"""


if __name__ == "__main__":
    print("=" * 60)
    print("EXERCISE 3A: Structured Contract Analysis")
    print("=" * 60)
    result = analyze_contract(SAMPLE_CONTRACT)
    print(json.dumps(result, indent=2))

    print("\n" + "=" * 60)
    print("EXERCISE 3B: Document Analysis Business Model")
    print("=" * 60)
    print("""
This pipeline is the foundation of a legal document AI business:

Revenue model:
  - Per document: $2-10/contract (vs $600-2000 for attorney review)
  - Subscription: $299-999/month for law firms

Cost per contract analysis:
  - ~4,000 input tokens + ~1,000 output tokens
  - At Opus 4.8 rates: ~$0.045 per contract
  - Margin at $5/contract: 99%

Scale scenario:
  - 100 law firm customers
  - Each reviews 200 contracts/month
  - At $5/contract: $100,000 MRR
  - Model costs: ~$900/month
  - Gross margin: 99%

The key moat: quality of extraction + industry-specific customization
(standard clauses, specific clause libraries, firm's risk preferences)
""")

    print("=" * 60)
    print("EXERCISE 3C: Batch Processing Cost Savings")
    print("=" * 60)
    print("""
If processing 10,000 contracts/month:

Standard API:
  - 10,000 × $0.045 = $450/month

Batch API (50% discount):
  - 10,000 × $0.0225 = $225/month

Savings: $225/month = $2,700/year
At scale (100,000 contracts): $2,250/month saved

Batch API trade-off: async processing (results within 24 hours)
vs. real-time. Use batch for overnight processing jobs.
    """)
