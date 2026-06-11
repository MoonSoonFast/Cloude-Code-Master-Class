# Tool Use — The Core Business Primitive

## Why Tool Use Is the Most Important Concept

Without tool use, Claude is a text-in, text-out system. Useful, but limited.

With tool use, Claude becomes an **agent that can do things in the world**: search the internet, run code, query databases, call APIs, read/write files, send emails — anything you connect to it.

Every serious business application built on Claude uses tool use.

---

## How Tool Use Works (The Loop)

```
1. You send: message + list of available tools
2. Claude responds with: "I want to call tool X with these arguments"
3. You execute the tool in your code
4. You send back: tool result
5. Claude continues, possibly calling more tools
6. Claude sends final text response when done
```

This loop repeats until Claude sends a response without a tool call.

### In Code (Python)

```python
import anthropic

client = anthropic.Anthropic()

tools = [
    {
        "name": "search_web",
        "description": "Search the web for current information",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Search query"}
            },
            "required": ["query"]
        }
    }
]

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    tools=tools,
    messages=[{"role": "user", "content": "What's the latest news about AI?"}]
)

# Check if Claude wants to use a tool
if response.stop_reason == "tool_use":
    for block in response.content:
        if block.type == "tool_use":
            tool_name = block.name
            tool_input = block.input
            # Execute tool_name with tool_input in your code
            # Then send result back to continue the loop
```

---

## Tool Design Principles

### 1. Atomic Tools (One Job Each)
Bad: `do_research_and_write_email(topic)`
Good: `search_web(query)` + `send_email(to, subject, body)`

Claude reasons better when tools have single, clear responsibilities.

### 2. Rich Descriptions
The description field is read by Claude to decide when to use the tool. Write it for Claude, not for humans:

Bad: `"search_web": "search"`
Good: `"search_web": "Search the web for current, real-time information. Use when you need facts that may have changed recently, current events, prices, or information not in your training data."`

### 3. Explicit Input Schemas
Use JSON Schema fully. Mark required fields. Add property descriptions:

```json
{
    "type": "object",
    "properties": {
        "query": {
            "type": "string",
            "description": "Search terms. Use specific, targeted queries for better results."
        },
        "max_results": {
            "type": "integer",
            "description": "Number of results to return (1-10)",
            "default": 5
        }
    },
    "required": ["query"]
}
```

---

## Server-Side Tools (Anthropic Hosts These)

Beyond user-defined tools, Anthropic provides tools that run on their infrastructure — no execution code needed on your side.

### Web Search
```python
tools = [{"type": "web_search_20250305", "name": "web_search"}]
```
Claude searches the internet and synthesizes results. Available in Managed Agents by default.

### Code Execution
```python
tools = [{"type": "code_execution_20250522", "name": "code_execution"}]
```
Claude writes and runs Python code on Anthropic's servers. Returns stdout, files, charts. No sandbox setup needed.

### Computer Use
```python
tools = [
    {"type": "computer_20250124", "name": "computer", "display_width_px": 1280, "display_height_px": 800}
]
```
Claude sees screenshots, moves mouse, types, clicks. Can operate any GUI software.
(Can also be self-hosted — Anthropic provides a Docker reference implementation.)

### Memory
```python
tools = [{"type": "memory_20250130", "name": "memory"}]
```
Persistent cross-session key-value store. Claude can save and recall information between completely separate conversations.

### Web Fetch
```python
tools = [{"type": "web_fetch_20250124", "name": "web_fetch"}]
```
Fetches and reads specific URLs. Different from web search — targeted at known URLs rather than searching.

---

## The Tool Runner — Auto-Loop Handling

Writing the tool execution loop manually is repetitive. The SDK's tool runner handles it:

```python
from anthropic import Anthropic
from anthropic.beta import BetaToolRunner

client = Anthropic()

# Define tools as Python functions with decorators
@beta_tool
def search_database(query: str, table: str) -> dict:
    """Search the internal database. Use for customer data, orders, and inventory."""
    return db.query(query, table)  # your actual implementation

# Tool runner handles the entire loop automatically
response = client.beta.messages.create_with_tool_runner(
    model="claude-opus-4-8",
    max_tokens=4096,
    tools=[search_database],
    messages=[{"role": "user", "content": "How many orders were placed last week?"}]
)
# response is the final text response after all tool calls complete
```

---

## Business Translation: What Tool Use Enables

| Tool Type | What You Can Build |
|---|---|
| Database query tools | Natural language database queries for non-technical users |
| API integration tools | AI that can take actions in your existing software stack |
| File read/write tools | Automated document processing pipelines |
| Email/calendar tools | AI executive assistant that actually does things |
| Web search tools | Research agents that synthesize real-time information |
| Code execution tools | Automated data analysis and report generation |
| Computer use | Automation of any legacy software with a GUI |
| Memory tools | Personalized AI that learns your users' preferences |

The key insight: **your tools define what problems your product can solve**. The richer your tool set, the more valuable your product.
