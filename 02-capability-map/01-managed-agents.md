# Managed Agents — Anthropic Runs the Loop

## The Core Concept

With standard Claude API, you write the agent loop yourself:
- Send message → get tool call → execute tool → send result → repeat → get final answer

With Managed Agents, Anthropic runs that loop for you in their infrastructure:
- You define an agent configuration (tools, instructions, model)
- Anthropic creates a persistent agent object with an ID
- Each task creates a "session" — Anthropic handles execution
- You get back a stream of events and a final result

You do not manage containers, tool execution infrastructure, or the agentic loop.

---

## Why This Matters

The hard part of building an agent product is not the prompting — it is the **infrastructure**:
- Reliable tool execution environment
- State management across a long multi-step task
- Per-task isolation (session containers)
- Streaming event handling for UX
- Error recovery and retry logic

Managed Agents hands all of this to Anthropic. You focus on the use case.

---

## Key Concepts

### Agent (Persistent Configuration)
An Agent is a named, versioned configuration object:
```json
{
  "name": "legal-document-reviewer",
  "model": "claude-opus-4-8",
  "instructions": "You are an expert legal document reviewer...",
  "tools": ["web_search", "code_execution", "memory"],
  "thinking": {"type": "adaptive"}
}
```
Create once, reference by ID forever. Do not create agents in the request path — they are long-lived objects.

### Session (One Task Execution)
A Session is a single invocation of an agent:
- Tied to a specific agent ID
- Gets its own isolated container (file system, environment)
- Streams events (tool calls, results, thinking, output)
- Has its own memory scope (can persist to agent memory or be ephemeral)

```python
session = client.beta.agents.sessions.create(
    agent_id="agent_abc123",
    input={"content": "Review this contract and flag any unusual clauses", "files": [file_id]}
)
```

### Environment
The per-session container where tools execute. Has:
- Isolated file system (mount files before session starts)
- Python execution environment
- Network access (if web tools enabled)
- Ephemeral by default (destroyed after session)

---

## Managed Agents vs. DIY Agents

| Aspect | DIY (Claude API + Tool Use) | Managed Agents |
|---|---|---|
| Tool execution | You implement and host | Anthropic hosts |
| Session isolation | Your responsibility | Automatic per-session containers |
| State management | Your code | Built-in |
| Streaming | Your SSE handling | Built-in event stream |
| Scaling | Your infrastructure | Anthropic scales |
| Flexibility | Maximum | Within Anthropic's tool set |
| Available tools | Anything you build | Anthropic-provided + MCP |
| Cost | Model cost only | Model cost + execution cost |

**Use Managed Agents when:** You want to build quickly, you don't need custom tool execution environments, and you're fine using Anthropic-provided tools.

**Use DIY agents when:** You need to call internal APIs, run proprietary code, integrate with private data sources, or need custom execution environments.

---

## Skills and MCP in Managed Agents

Agents can use **Skills** — pre-built capability packages:
- Computer Use
- Web research
- Code execution
- File operations

And **MCP servers** — any third-party tool via the Model Context Protocol:
- GitHub (code access)
- Slack (messaging)
- Google Drive (documents)
- Custom internal APIs (via your own MCP server)

---

## The Anthropic CLI (for Managed Agents)

The `ant` CLI tool lets you define agents in YAML and deploy from the command line:

```yaml
# agent.yaml
name: research-analyst
model: claude-opus-4-8
instructions: |
  You are an expert research analyst. Given a topic, produce a structured
  analysis report with key findings, market data, and strategic implications.
tools:
  - web_search
  - code_execution
  - memory
thinking:
  type: adaptive
```

```bash
ant agents create --file agent.yaml  # Returns agent ID
ant sessions run --agent-id agent_xyz --input "Analyze the no-code tools market"
```

---

## Business Opportunities Managed Agents Unlock

Because Anthropic handles the infrastructure, you can ship these products faster:

1. **Autonomous research service** — Users submit research questions; agent researches, analyzes, and delivers reports
2. **Document processing pipelines** — Upload contracts/invoices/forms; agent extracts, validates, routes
3. **Competitive intelligence service** — Agent monitors competitor websites, pricing, job postings, releases
4. **Automated data analysis** — Upload datasets; agent analyzes, generates insights, creates visualizations
5. **AI code review** — Agents review PRs, security audit codebases, suggest refactors

The barrier to shipping these is not infrastructure anymore — it is finding the right use case and distribution channel.
