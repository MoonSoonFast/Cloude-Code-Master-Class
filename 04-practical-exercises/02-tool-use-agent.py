"""
Exercise 2: Build a Research Agent with Tool Use
Goal: Understand the tool use loop, how Claude decides to use tools,
      and how to build a useful agent from scratch.

This builds a "business opportunity researcher" — give it a topic,
it uses tools to gather information and produce a structured report.

pip install anthropic
export ANTHROPIC_API_KEY=your_key_here
"""

import anthropic
import json
from datetime import datetime

client = anthropic.Anthropic()

# ============================================================
# Tool Implementations (these are your "backend functions")
# ============================================================

def search_market_data(query: str, focus: str = "market_size") -> dict:
    """Simulated tool — in production, call a real data API."""
    data = {
        "query": query,
        "focus": focus,
        "results": [
            {
                "source": "Gartner",
                "finding": f"Market for {query} estimated at $12B in 2024, growing 28% CAGR",
                "date": "2024-Q4"
            },
            {
                "source": "McKinsey",
                "finding": f"AI automation in {query} space could displace 40% of current labor",
                "date": "2024-11"
            }
        ]
    }
    return data


def analyze_competitors(market: str) -> dict:
    """Simulated competitor analysis tool."""
    return {
        "market": market,
        "competitors": [
            {"name": "Established Player A", "funding": "$150M", "weakness": "Enterprise-only, high price"},
            {"name": "Startup B", "funding": "$8M", "weakness": "Narrow use case, poor UX"},
        ],
        "gap": f"No strong solution for mid-market {market} (10-100 seat teams)",
        "market_maturity": "early"
    }


def estimate_unit_economics(product_type: str, target_price: float, ai_calls_per_user_month: int) -> dict:
    """Calculate whether a business model is viable."""
    # Estimate AI costs
    avg_tokens_per_call = 3000  # input + output
    cost_per_call = (avg_tokens_per_call / 1_000_000) * 25  # rough Opus rate
    monthly_ai_cost_per_user = cost_per_call * ai_calls_per_user_month

    margin = (target_price - monthly_ai_cost_per_user) / target_price * 100

    return {
        "product_type": product_type,
        "target_price_per_user_month": target_price,
        "ai_cost_per_user_month": round(monthly_ai_cost_per_user, 2),
        "gross_margin_pct": round(margin, 1),
        "viable": margin > 50,
        "recommendation": "Viable" if margin > 70 else "Tight margins — optimize or reprice" if margin > 40 else "Not viable at this price"
    }


# ============================================================
# Tool Schema (Claude reads this to decide when to call tools)
# ============================================================

TOOLS = [
    {
        "name": "search_market_data",
        "description": "Search for market size, growth rates, and trends for a given market segment. Use this to quantify opportunity size.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The market segment or topic to research (e.g., 'AI document processing for law firms')"
                },
                "focus": {
                    "type": "string",
                    "enum": ["market_size", "growth_rate", "adoption_stage"],
                    "description": "What aspect of the market to focus on"
                }
            },
            "required": ["query"]
        }
    },
    {
        "name": "analyze_competitors",
        "description": "Analyze the competitive landscape for a market. Returns existing players, their weaknesses, and market gaps.",
        "input_schema": {
            "type": "object",
            "properties": {
                "market": {
                    "type": "string",
                    "description": "The market to analyze for competitive dynamics"
                }
            },
            "required": ["market"]
        }
    },
    {
        "name": "estimate_unit_economics",
        "description": "Calculate whether a product business model is financially viable. Use after identifying the product type and target price.",
        "input_schema": {
            "type": "object",
            "properties": {
                "product_type": {"type": "string"},
                "target_price": {"type": "number", "description": "Monthly price per user in USD"},
                "ai_calls_per_user_month": {"type": "integer", "description": "Estimated number of AI API calls per user per month"}
            },
            "required": ["product_type", "target_price", "ai_calls_per_user_month"]
        }
    }
]


# ============================================================
# The Tool Use Loop
# ============================================================

def run_agent(user_query: str) -> str:
    """Run the agent loop until Claude stops calling tools."""

    messages = [{"role": "user", "content": user_query}]

    print(f"\nUser: {user_query}\n")
    print("=" * 50)

    tool_call_count = 0

    while True:
        response = client.messages.create(
            model="claude-opus-4-8",
            max_tokens=4096,
            thinking={"type": "adaptive"},
            system="""You are a business opportunity analyst with expertise in AI products.
            When asked to research an opportunity, ALWAYS:
            1. Search for market data first
            2. Analyze competition
            3. Calculate unit economics
            4. Then synthesize a clear recommendation

            Be specific with numbers. Format your final report clearly.""",
            tools=TOOLS,
            messages=messages
        )

        # If Claude wants to call tools
        if response.stop_reason == "tool_use":
            # Collect all tool calls in this response
            tool_calls = [block for block in response.content if block.type == "tool_use"]
            text_blocks = [block for block in response.content if block.type == "text"]

            for text in text_blocks:
                if text.text.strip():
                    print(f"[Claude thinking aloud]: {text.text[:200]}...")

            # Execute each tool and collect results
            tool_results = []
            for tool_call in tool_calls:
                tool_call_count += 1
                print(f"\n→ Tool call #{tool_call_count}: {tool_call.name}({json.dumps(tool_call.input, indent=2)})")

                # Dispatch to the right function
                if tool_call.name == "search_market_data":
                    result = search_market_data(**tool_call.input)
                elif tool_call.name == "analyze_competitors":
                    result = analyze_competitors(**tool_call.input)
                elif tool_call.name == "estimate_unit_economics":
                    result = estimate_unit_economics(**tool_call.input)
                else:
                    result = {"error": f"Unknown tool: {tool_call.name}"}

                print(f"← Result: {json.dumps(result, indent=2)}")

                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": tool_call.id,
                    "content": json.dumps(result)
                })

            # Add Claude's response and tool results to history, continue loop
            messages.append({"role": "assistant", "content": response.content})
            messages.append({"role": "user", "content": tool_results})

        else:
            # Claude is done calling tools — extract final text response
            final_text = ""
            for block in response.content:
                if hasattr(block, "text"):
                    final_text += block.text

            print(f"\n{'=' * 50}")
            print(f"FINAL REPORT (after {tool_call_count} tool calls):")
            print(f"{'=' * 50}")
            print(final_text)

            print(f"\nTokens used: {response.usage.input_tokens} in / {response.usage.output_tokens} out")
            return final_text


if __name__ == "__main__":
    # Run the agent on a business research question
    run_agent(
        "Research the opportunity for building an AI document processing tool for mid-market law firms. "
        "I'm thinking about charging $499/month with roughly 200 AI calls per user per month. Is this viable?"
    )
