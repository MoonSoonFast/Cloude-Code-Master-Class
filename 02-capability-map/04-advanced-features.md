# Advanced Claude Features — The Power User Toolkit

## Structured Outputs

Claude can return guaranteed-valid JSON matching a schema you define. No parsing errors, no hallucinated fields.

```python
from anthropic import Anthropic

client = Anthropic()

# Method 1: JSON Schema enforcement via output_config
response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    output_config={
        "format": {
            "type": "json_schema",
            "json_schema": {
                "name": "company_analysis",
                "schema": {
                    "type": "object",
                    "properties": {
                        "company_name": {"type": "string"},
                        "industry": {"type": "string"},
                        "revenue_estimate": {"type": "number"},
                        "key_risks": {"type": "array", "items": {"type": "string"}},
                        "opportunity_score": {"type": "integer", "minimum": 1, "maximum": 10}
                    },
                    "required": ["company_name", "industry", "key_risks", "opportunity_score"]
                }
            }
        }
    },
    messages=[{"role": "user", "content": "Analyze Stripe as a business."}]
)

# Method 2: messages.parse() — validates automatically
response = client.messages.parse(
    model="claude-opus-4-8",
    max_tokens=1024,
    output_config={"format": {"type": "json_schema", "json_schema": {...}}},
    messages=[...]
)
# response.content is now validated against your schema
```

### Business Use Cases
- Extract structured data from unstructured documents (invoices, resumes, contracts)
- API responses that downstream systems consume directly
- Any pipeline where type safety matters

---

## Vision (Image Understanding)

Claude can read images in requests. Send screenshots, photos, documents, charts — Claude reasons about them.

```python
import base64
with open("invoice.png", "rb") as f:
    image_data = base64.standard_b64encode(f.read()).decode("utf-8")

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": [
            {
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": "image/png",
                    "data": image_data
                }
            },
            {"type": "text", "text": "Extract all line items, amounts, and vendor information from this invoice."}
        ]
    }]
)
```

### Supported Formats
- JPEG, PNG, GIF, WebP
- PDF (via Files API — multiple pages)
- URL-referenced images: `{"type": "url", "url": "https://..."}`

### Business Use Cases
- Invoice/receipt processing
- ID document verification
- Medical image analysis (with appropriate disclaimers)
- Chart/graph data extraction
- Form digitization
- Visual QA/testing

---

## Files API

Upload files once, reference them multiple times across requests. No re-uploading the same document on every call.

```python
# Upload once
with open("annual_report.pdf", "rb") as f:
    file_response = client.beta.files.upload(
        file=("annual_report.pdf", f, "application/pdf")
    )
file_id = file_response.id  # Save this ID

# Reference in any future request
response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=2048,
    messages=[{
        "role": "user",
        "content": [
            {"type": "document", "source": {"type": "file", "file_id": file_id}},
            {"type": "text", "text": "What are the key revenue figures?"}
        ]
    }]
)
```

### Why This Matters
- Large documents (PDFs, CSVs, reports) only pay upload bandwidth once
- Reuse across multiple analytical questions without re-uploading
- Enables async workflows: upload files in batch, analyze later

---

## Batch Processing

Process thousands of requests asynchronously at **50% reduced cost**.

```python
# Create a batch of requests
batch = client.messages.batches.create(
    requests=[
        {
            "custom_id": f"request_{i}",
            "params": {
                "model": "claude-opus-4-8",
                "max_tokens": 500,
                "messages": [{"role": "user", "content": text}]
            }
        }
        for i, text in enumerate(texts_to_process)
    ]
)

# Check status later
batch_status = client.messages.batches.retrieve(batch.id)
if batch_status.processing_status == "ended":
    for result in client.messages.batches.results(batch.id):
        print(result.custom_id, result.result.message.content)
```

### When to Use Batches
- Processing large datasets (10K+ documents)
- Overnight data enrichment jobs
- Training data generation
- Bulk classification or extraction
- Any task where latency doesn't matter and cost does

**50% cost reduction** is massive for high-volume workloads. A task that costs $1,000 normally costs $500 in batch mode.

---

## Streaming

Get tokens as they're generated rather than waiting for the full response. Critical for user-facing applications.

```python
with client.messages.stream(
    model="claude-opus-4-8",
    max_tokens=2048,
    messages=[{"role": "user", "content": "Write a detailed analysis..."}]
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
    
    # Get full final message after streaming
    final_message = stream.get_final_message()
```

### Business Importance
- Without streaming: user stares at blank screen for 15-30 seconds
- With streaming: user sees output immediately, perceives the product as fast
- For long outputs (reports, documents), streaming is mandatory for UX

---

## Memory Stores (Cross-Session Persistence)

Claude can remember information across completely separate conversations.

```python
tools = [{"type": "memory_20250130", "name": "memory"}]

# First session — Claude learns about user
client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=tools,
    messages=[{
        "role": "user",
        "content": "I'm a lawyer specializing in IP law. I prefer concise answers."
    }]
)

# Later session — Claude remembers (no context passed)
client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=tools,
    messages=[{
        "role": "user",
        "content": "What do I need to know about the recent SCOTUS IP ruling?"
    }]
    # Claude will recall user's profession and communication preference
)
```

### Business Implications
- Personalization without managing user profiles manually
- AI assistants that get better the more users interact with them
- Preference/context that survives across chat sessions
- Can store: communication style, domain knowledge, ongoing projects, past decisions

---

## Scheduled Deployments (Autonomous Agents)

Run Claude agents on a cron schedule with no human trigger. True autonomous operation.

Configure via Anthropic Console:
- Set a cron expression (e.g., `0 9 * * 1-5` = every weekday at 9 AM)
- Point to a Managed Agent
- Define the recurring task

The agent wakes up, does its job, and goes back to sleep.

### Business Use Cases
- Daily competitor monitoring reports delivered to Slack
- Weekly data quality checks on your database
- Automated client status reports
- Overnight data enrichment pipelines
- Regular SEO content audits
- Recurring financial reconciliation

This is essentially cron jobs + AI. The market for automated intelligence delivery is enormous.

---

## Token Counting (Pre-Request Cost Estimation)

```python
# Count tokens before sending — no charge for counting
count = client.messages.count_tokens(
    model="claude-opus-4-8",
    messages=[{"role": "user", "content": very_long_document}]
)
print(f"This request will use {count.input_tokens} input tokens")
# Estimated cost: count.input_tokens / 1_000_000 * 5.00
```

Use this in your product to:
- Show users estimated cost before running expensive operations
- Implement usage limits
- Optimize prompts before they go to production
- Gate requests that exceed your cost threshold
