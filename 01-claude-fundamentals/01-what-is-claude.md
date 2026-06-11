# What Is Claude — The Accurate Mental Model

## The Wrong Mental Model (Don't Think This)

> "Claude is a chatbot I send messages to."

This mental model caps your thinking. You will only build chat apps.

## The Right Mental Model

> "Claude is a **programmable reasoning process** with a 1-million-token working memory that can call tools, run code, browse the web, control software, persist state, and execute on a schedule — accessed via HTTP."

This mental model opens up every business opportunity in this repository.

---

## The Three Surfaces

Anthropic ships Claude through three distinct surfaces:

### 1. Claude API (for developers — this is your primary tool)
- Full programmatic control via HTTP / official SDKs
- You build the application; Claude is the reasoning layer
- Everything in this repo focuses here

### 2. Claude Code (CLI tool for software development)
- Terminal-based agent for writing, editing, running code
- Deep IDE integration (VS Code, JetBrains)
- Has its own hooks, slash commands, MCP server support
- Key insight: **Claude Code IS built on the Claude API** — it's a reference implementation of an agentic coding tool

### 3. Claude.ai (consumer product)
- Anthropic's own end-user product
- Not programmable (no API access through this surface)
- Useful for understanding what non-technical users expect

---

## How the API Actually Works

Every Claude request goes through a single endpoint:

```
POST https://api.anthropic.com/v1/messages
```

That's it. Everything — tool use, vision, extended thinking, streaming, structured outputs — is a feature of this one endpoint. There is no separate "tool use endpoint" or "vision endpoint."

### The Request Shape

```json
{
  "model": "claude-opus-4-8",
  "max_tokens": 4096,
  "messages": [
    {"role": "user", "content": "..."}
  ]
}
```

### Key Request Parameters

| Parameter | What It Does | Business Relevance |
|---|---|---|
| `model` | Which Claude model | Cost vs. quality tradeoff |
| `max_tokens` | Max tokens in response | Limits output length |
| `system` | System prompt | Sets agent personality/role |
| `tools` | Available tools | Enables agent capabilities |
| `thinking` | Adaptive thinking mode | Better reasoning, more tokens |
| `stream` | Streaming responses | Better UX, avoids timeouts |

---

## The Token Economy — Master This

Everything in Claude is measured in **tokens** (roughly 4 characters = 1 token).

You pay for:
- **Input tokens**: everything you send (system prompt + conversation history + tool results)
- **Output tokens**: everything Claude writes back (3-5x more expensive than input)

### The Hidden Cost Driver: Context Accumulation

In a multi-turn conversation, you resend the **entire conversation history** every turn. This means:
- Turn 1: 500 tokens
- Turn 10: 5,000+ tokens  
- Turn 50: 25,000+ tokens

**Business implication:** For high-volume, multi-turn applications, context accumulation destroys margins. Solutions: prompt caching, conversation summarization, or switching to Haiku for high-volume low-complexity tasks.

### Prompt Caching: The Margin Saver

When a prefix of your prompt is identical across requests, Anthropic caches it:
- Cache write: 25% more than normal input price (one-time)
- Cache read: 90% cheaper than normal input price

If your system prompt is 10,000 tokens and you run 1,000 requests/day:
- Without caching: 10,000 × 1,000 × $5/1M = **$50/day** just for the system prompt
- With caching: $50 once (write) + $5/day (reads) → **90% cost reduction**

**Business implication:** Any product with a large static system prompt (instructions, context, data) should use prompt caching. It's the difference between a viable and non-viable unit economics model.

---

## Claude's Reasoning Capabilities

### Standard Mode
Claude reads your input, thinks implicitly, responds. Fast, cheap.

### Adaptive Thinking (`thinking: {type: "adaptive"}`)
Claude explicitly "thinks before answering" — like showing work. The reasoning process is visible as `thinking` blocks before the final response. Claude decides dynamically how much thinking to apply based on task complexity.

- Costs more tokens (thinking tokens are billed)
- Significantly better for: math, logic, complex planning, multi-step reasoning
- Required for: hard coding problems, complex analysis, strategy tasks

**Use case trigger:** Any task where a smart human would "stop and think carefully before answering" should use adaptive thinking.

### Effort Parameter (Fable 5 only)
`output_config.effort`: `low`, `medium`, `high`, `xhigh`, `max`

Controls depth of reasoning on the most powerful model. Use `max` for the hardest research and strategy work.

---

## Context Window: 1 Million Tokens

Most models offer 200K-300K context. Claude offers **1M tokens** (all except Haiku 4.5 which offers 200K).

What fits in 1M tokens:
- Entire codebases (most products)
- Thousands of research papers
- Complete legal document sets
- Multi-year email histories
- Full medical records

**Business implication:** Any "analyze our entire knowledge base / codebase / document set" use case is technically feasible with Claude where it isn't with competitors. This is a moat.

---

## The Stateless Default

By default, Claude has **no memory between API calls**. Each request starts fresh. If you want continuity, you must either:

1. **Pass conversation history** in each request (simple but gets expensive)
2. **Use Memory Stores** (persistent cross-session memory — covered in Module 2)
3. **Use Managed Agents** (Anthropic manages session state — covered in Module 2)

This is crucial for product architecture decisions.
