# Models and Pricing — Strategic Cost Analysis

## Current Model Lineup (as of June 2026)

| Model | ID | Context | Input $/M | Output $/M | Best For |
|---|---|---|---|---|---|
| Claude Fable 5 | `claude-fable-5` | 1M | $10 | $50 | Most complex tasks |
| Claude Opus 4.8 | `claude-opus-4-8` | 1M | $5 | $25 | Default; best balance |
| Claude Sonnet 4.6 | `claude-sonnet-4-6` | 1M | $3 | $15 | Mid-tier quality/cost |
| Claude Haiku 4.5 | `claude-haiku-4-5` | 200K | $1 | $5 | High-volume, fast |

**Default for building:** Use `claude-opus-4-8` unless you have a specific reason not to.

---

## Understanding the Real Cost of a Request

The posted prices are per million tokens. Here's what that means practically:

### Typical Request Sizes

| Task | Input Tokens | Output Tokens | Opus 4.8 Cost |
|---|---|---|---|
| Simple classification | 200 | 20 | ~$0.000150 |
| Document summarization (10 pages) | 5,000 | 500 | ~$0.0375 |
| Complex code generation | 3,000 | 2,000 | ~$0.065 |
| Full codebase analysis (50K tokens) | 50,000 | 5,000 | ~$0.375 |
| Extended agent session (100K ctx) | 100,000 | 10,000 | ~$0.75 |

### Monthly Cost at Scale

If you run 10,000 requests/day with average 2,000 input + 500 output tokens:

| Model | Monthly Cost |
|---|---|
| Haiku 4.5 | ~$450/mo |
| Sonnet 4.6 | ~$1,350/mo |
| Opus 4.8 | ~$2,250/mo |
| Fable 5 | ~$4,500/mo |

At $50-200/user/month SaaS pricing, you need 3-10+ paying users to cover model costs at scale. The margin math works.

---

## Model Selection Strategy

### Use Haiku 4.5 when:
- High volume (10K+ requests/day)
- Task is classification, extraction, or simple summarization
- Latency is critical (Haiku is fastest)
- User is waiting in real-time for short outputs

### Use Sonnet 4.6 when:
- Moderate complexity tasks
- Need better reasoning than Haiku but cost matters
- Building B2B tools where quality matters but margins are tight

### Use Opus 4.8 when (default choice):
- Complex reasoning, analysis, strategy
- Coding tasks
- Writing quality matters
- Building the first version of anything (optimize later)

### Use Fable 5 when:
- Hardest reasoning tasks in your stack
- Long-horizon planning
- Customer-facing flagship features where quality is the product
- Research tasks that need maximum depth

---

## The Cascading Model Architecture

The best production systems use multiple models strategically:

```
User Request
    ↓
[Haiku] Route and classify the request (cheap, fast)
    ↓
    ├── Simple task → [Haiku] Handle directly
    ├── Medium task → [Sonnet] Handle
    └── Complex task → [Opus/Fable] Handle
                           ↓
                    [Haiku] Post-process and format output
```

This architecture can reduce costs 60-80% vs. running everything on Opus while maintaining quality where it matters.

---

## Fable 5 — The Differentiator

Fable 5 is architecturally different from the Opus family. Key behaviors:

### Always-On Thinking
Thinking cannot be disabled. You cannot set `thinking: {type: "disabled"}` — it will return a 400 error. Thinking is always adaptive. Control depth with `output_config.effort`.

### Refusal Stop Reason
Unlike other models, Fable 5 may refuse mid-generation:
- HTTP 200 response (not an error code)
- `stop_reason: "refusal"` in the response
- Pre-generation refusals: empty content, not billed
- Mid-stream refusals: billed for tokens already generated

**You must check `stop_reason` before reading `content` when using Fable 5.**

### 30-Day Data Retention Required
Fable 5 is not available under zero data retention configurations. If your product has a compliance requirement for zero retention, you cannot use Fable 5.

### No Assistant Prefill
You cannot start Claude's response with a partial string (no assistant-turn prefilling). This affects certain structured output techniques.

---

## Pricing Strategy for Your Business

### The Margin Formula

```
Revenue per request > (Input tokens × input price) + (Output tokens × output price) + overhead
```

For a $99/month SaaS with 1,000 requests/user/month:
- Revenue per request: $0.099
- Available for model cost: ~$0.05 (50% margin target)
- At Opus 4.8 rates: 2,000 input + 500 output tokens = $0.0225 per request ✓

The math works for most SaaS pricing models — AI model costs are NOT the barrier people think they are.

### When Model Costs Actually Break You

Model costs become a problem when:
1. Your users run **very long sessions** (100K+ token contexts per session)
2. You have very high output-to-revenue ratios (free tier abuse)
3. You're competing on price in a commodity market

Solutions: context limits, output caps, tiered pricing, prompt caching.
