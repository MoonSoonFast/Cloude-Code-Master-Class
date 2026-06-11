"""
Exercise 4: Competitive Intelligence Agent
Goal: Build the MVP of Opportunity #2 from the business analysis.

This is the closest exercise to a real, shippable product.
It uses: tool use, memory (simulated), adaptive thinking, structured outputs.

pip install anthropic
export ANTHROPIC_API_KEY=your_key_here
"""

import anthropic
import json
from datetime import datetime

client = anthropic.Anthropic()

# ============================================================
# Simulated tools (replace with real implementations)
# In production: use Brave Search API, Firecrawl, or Playwright
# ============================================================

def search_news(query: str, days_back: int = 7) -> dict:
    """Search for recent news about a company or topic."""
    # Production: use Brave Search API or similar
    return {
        "query": query,
        "results": [
            {
                "title": f"[Simulated] {query} announces new pricing tier",
                "date": "2025-01-08",
                "source": "TechCrunch",
                "summary": "Company launches mid-market pricing at $299/seat",
                "url": "https://example.com/article1"
            },
            {
                "title": f"[Simulated] {query} raises Series B",
                "date": "2025-01-05",
                "source": "Crunchbase",
                "summary": "$45M round led by a16z, focus on enterprise expansion",
                "url": "https://example.com/article2"
            }
        ]
    }


def get_job_postings(company: str) -> dict:
    """Scrape job postings to infer strategic priorities."""
    # Production: use LinkedIn API, Indeed API, or scraping
    return {
        "company": company,
        "postings": [
            {"title": "Senior ML Engineer - NLP", "department": "Engineering", "signal": "Investing in better models"},
            {"title": "Enterprise Account Executive", "department": "Sales", "signal": "Moving upmarket"},
            {"title": "Head of International Expansion", "department": "Ops", "signal": "Geographic expansion plans"}
        ],
        "total_open_roles": 23,
        "growth_signal": "hiring_aggressively"
    }


def check_pricing_page(company_url: str) -> dict:
    """Fetch and parse competitor pricing."""
    # Production: use Playwright or Firecrawl to get real pricing
    return {
        "url": company_url,
        "pricing_tiers": [
            {"name": "Starter", "price": "$49/mo", "users": "1-5"},
            {"name": "Pro", "price": "$199/mo", "users": "6-25"},
            {"name": "Enterprise", "price": "Custom", "users": "25+"}
        ],
        "last_change": "2024-11-15",
        "change_detected": False
    }


def get_product_releases(company: str) -> dict:
    """Check for new product releases or feature announcements."""
    return {
        "company": company,
        "recent_releases": [
            {
                "date": "2025-01-03",
                "announcement": "API v3 with batch processing support",
                "significance": "Expanding technical user base"
            }
        ]
    }


TOOLS = [
    {
        "name": "search_news",
        "description": "Search for recent news about a company. Use to find press releases, funding announcements, and industry coverage.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Company name + relevant terms"},
                "days_back": {"type": "integer", "description": "How many days back to search", "default": 7}
            },
            "required": ["query"]
        }
    },
    {
        "name": "get_job_postings",
        "description": "Analyze a company's job postings to infer strategic priorities. Useful for understanding where competitors are investing.",
        "input_schema": {
            "type": "object",
            "properties": {
                "company": {"type": "string"}
            },
            "required": ["company"]
        }
    },
    {
        "name": "check_pricing_page",
        "description": "Fetch and analyze a competitor's pricing page. Use to detect pricing changes.",
        "input_schema": {
            "type": "object",
            "properties": {
                "company_url": {"type": "string", "description": "URL of the company's pricing page"}
            },
            "required": ["company_url"]
        }
    },
    {
        "name": "get_product_releases",
        "description": "Check for recent product announcements and feature releases from a company.",
        "input_schema": {
            "type": "object",
            "properties": {
                "company": {"type": "string"}
            },
            "required": ["company"]
        }
    }
]


# ============================================================
# Intelligence Report Schema
# ============================================================

INTELLIGENCE_REPORT_SCHEMA = {
    "name": "competitive_intelligence_report",
    "schema": {
        "type": "object",
        "properties": {
            "company": {"type": "string"},
            "report_date": {"type": "string"},
            "threat_level": {
                "type": "string",
                "enum": ["low", "medium", "high", "critical"],
                "description": "How significant are this week's developments?"
            },
            "key_developments": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "development": {"type": "string"},
                        "category": {"type": "string", "enum": ["pricing", "product", "hiring", "funding", "partnerships", "expansion"]},
                        "strategic_implication": {"type": "string"},
                        "recommended_response": {"type": "string"}
                    },
                    "required": ["development", "category", "strategic_implication"]
                }
            },
            "strategic_summary": {"type": "string"},
            "action_items": {"type": "array", "items": {"type": "string"}}
        },
        "required": ["company", "report_date", "threat_level", "key_developments", "strategic_summary"]
    }
}


def run_competitive_analysis(our_company: str, competitor: str, competitor_url: str) -> dict:
    """
    Full competitive intelligence run for one competitor.
    In production, this would run on a schedule (daily/weekly).
    """

    system = f"""You are a strategic intelligence analyst for {our_company}.
    Your job is to monitor competitors and synthesize intelligence into actionable briefings.

    For every development you discover:
    1. Explain what it means strategically (not just what happened)
    2. Identify if it threatens us, creates opportunity, or is neutral
    3. Suggest a concrete response if warranted

    Be direct. No fluff. Every sentence should inform a decision."""

    messages = [{
        "role": "user",
        "content": f"""Conduct a comprehensive competitive intelligence review of {competitor}.

        Research:
        1. Recent news (last 7 days)
        2. Job postings (what are they hiring for?)
        3. Current pricing (any changes?)
        4. Recent product releases

        Then synthesize everything into a strategic briefing for our leadership team.
        Pricing page URL: {competitor_url}/pricing"""
    }]

    print(f"Running competitive intelligence on {competitor}...")

    # Run the agentic loop
    tool_calls_made = []

    while True:
        response = client.messages.create(
            model="claude-opus-4-8",
            max_tokens=4096,
            thinking={"type": "adaptive"},
            output_config={
                "format": {
                    "type": "json_schema",
                    "json_schema": INTELLIGENCE_REPORT_SCHEMA
                }
            } if False else None,  # Note: can't use both tool use AND structured output simultaneously
            system=system,
            tools=TOOLS,
            messages=messages
        )

        if response.stop_reason == "tool_use":
            tool_calls = [b for b in response.content if b.type == "tool_use"]
            results = []

            for tc in tool_calls:
                tool_calls_made.append(tc.name)
                print(f"  → {tc.name}({list(tc.input.values())[0] if tc.input else ''})")

                if tc.name == "search_news":
                    result = search_news(**tc.input)
                elif tc.name == "get_job_postings":
                    result = get_job_postings(**tc.input)
                elif tc.name == "check_pricing_page":
                    result = check_pricing_page(**tc.input)
                elif tc.name == "get_product_releases":
                    result = get_product_releases(**tc.input)
                else:
                    result = {"error": f"Unknown tool: {tc.name}"}

                results.append({
                    "type": "tool_result",
                    "tool_use_id": tc.id,
                    "content": json.dumps(result)
                })

            messages.append({"role": "assistant", "content": response.content})
            messages.append({"role": "user", "content": results})

        else:
            # Final synthesis
            final_text = "".join(b.text for b in response.content if hasattr(b, "text"))

            print(f"\n  Tools used: {', '.join(tool_calls_made)}")
            print(f"  Tokens: {response.usage.input_tokens} in / {response.usage.output_tokens} out")
            return {
                "competitor": competitor,
                "analysis": final_text,
                "tools_used": tool_calls_made
            }


if __name__ == "__main__":
    print("=" * 60)
    print("EXERCISE 4: Competitive Intelligence Agent")
    print("=" * 60)

    result = run_competitive_analysis(
        our_company="BuildWithAI Inc",
        competitor="Competitor Corp",
        competitor_url="https://competitorcorp.com"
    )

    print("\n" + "=" * 60)
    print("INTELLIGENCE REPORT")
    print("=" * 60)
    print(result["analysis"])

    print("\n" + "=" * 60)
    print("PRODUCTIZATION PATH")
    print("=" * 60)
    print("""
To turn this into a real product:

1. Replace simulated tools with real data sources:
   - search_news → Brave Search API ($3/month for 2K queries)
   - get_job_postings → LinkedIn scraping or RapidAPI job boards
   - check_pricing_page → Firecrawl or Playwright
   - get_product_releases → GitHub releases API + blog RSS feeds

2. Add scheduling (run every weekday morning):
   - Use Anthropic Scheduled Agents (Console) OR
   - Deploy as a cron job on any cloud provider

3. Add delivery:
   - Slack webhook to post briefing to #competitive-intel channel
   - Email via SendGrid

4. Build configuration UI:
   - Form to add/remove competitors
   - Configure which types of intelligence to track
   - Set alert thresholds (e.g., only alert if pricing changes)

5. Multi-tenant: each customer tracks their own competitor set

Pricing: $99/month for 3 competitors, $299 for unlimited
    """)
