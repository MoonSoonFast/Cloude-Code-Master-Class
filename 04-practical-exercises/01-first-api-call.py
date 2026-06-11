"""
Exercise 1: Your First Claude API Call
Goal: Understand the request/response cycle, token counting, and pricing

Before running:
  pip install anthropic
  export ANTHROPIC_API_KEY=your_key_here

After running: Check the console for token counts and cost estimates.
Notice how output tokens cost more than input tokens.
"""

import anthropic
import os

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))


def basic_request():
    """The simplest possible Claude request."""
    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "What is the main business opportunity in AI right now?"}
        ]
    )

    # Inspect the full response object
    print("=== RESPONSE STRUCTURE ===")
    print(f"Model used: {response.model}")
    print(f"Stop reason: {response.stop_reason}")
    print(f"Input tokens: {response.usage.input_tokens}")
    print(f"Output tokens: {response.usage.output_tokens}")

    # Calculate cost
    input_cost = (response.usage.input_tokens / 1_000_000) * 5.00   # $5/M for Opus 4.8
    output_cost = (response.usage.output_tokens / 1_000_000) * 25.00  # $25/M for Opus 4.8
    total_cost = input_cost + output_cost

    print(f"\n=== COST ===")
    print(f"Input cost:  ${input_cost:.6f}")
    print(f"Output cost: ${output_cost:.6f}")
    print(f"Total cost:  ${total_cost:.6f}")
    print(f"(At 1000 requests/day, this is ~${total_cost * 1000 * 30:.2f}/month)")

    print(f"\n=== RESPONSE ===")
    print(response.content[0].text)


def with_system_prompt():
    """Show how a system prompt adds tokens (and cost) to every request."""
    system = """You are a strategic business analyst specializing in AI opportunities.
    You give concise, specific answers focused on actionable insights.
    Always mention: market size, competition level, and technical feasibility."""

    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=1024,
        system=system,
        messages=[
            {"role": "user", "content": "What vertical should I target for my first AI product?"}
        ]
    )

    system_tokens = len(system) // 4  # rough estimate
    print(f"System prompt ~{system_tokens} tokens")
    print(f"If you run 1000 req/day: ~{system_tokens * 1000} system tokens/day")
    print(f"Monthly system prompt cost alone: ${(system_tokens * 1000 * 30 / 1_000_000) * 5:.2f}")
    print(f"\n→ Lesson: Long system prompts need prompt caching to be cost-effective at scale\n")
    print(response.content[0].text)


def count_tokens_before_sending():
    """Use token counting API to estimate cost before spending money."""
    messages = [
        {"role": "user", "content": "Analyze the competitive landscape of the AI document processing market in 2025."}
    ]

    count = client.messages.count_tokens(
        model="claude-opus-4-8",
        messages=messages
    )

    print(f"Input tokens: {count.input_tokens}")
    estimated_output = 800  # estimate
    input_cost = (count.input_tokens / 1_000_000) * 5.00
    output_cost = (estimated_output / 1_000_000) * 25.00

    print(f"Estimated cost: ${input_cost + output_cost:.6f}")
    print("→ Use token counting in production to gate expensive requests")


if __name__ == "__main__":
    print("=" * 60)
    print("EXERCISE 1A: Basic Request")
    print("=" * 60)
    basic_request()

    print("\n" + "=" * 60)
    print("EXERCISE 1B: System Prompt Cost Impact")
    print("=" * 60)
    with_system_prompt()

    print("\n" + "=" * 60)
    print("EXERCISE 1C: Pre-Request Token Counting")
    print("=" * 60)
    count_tokens_before_sending()
