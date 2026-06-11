"""
Exercise 5: Build Your Own MCP Server
Goal: Understand how to expose your data/tools to any Claude deployment.

This creates a minimal but functional MCP server for a "business data" use case.
Once deployed, this server can be connected to:
  - Claude Code (developers using the CLI)
  - Managed Agents (via API config)
  - Any MCP-compatible AI client

pip install mcp anthropic
"""

import asyncio
import json
from typing import Any
from mcp.server import Server
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
import mcp.types as types


# ============================================================
# Your business logic / data layer
# Replace these with real database queries, API calls, etc.
# ============================================================

SAMPLE_BUSINESS_DATA = {
    "customers": [
        {"id": "c001", "name": "Acme Corp", "revenue": 125000, "tier": "enterprise", "status": "active"},
        {"id": "c002", "name": "StartupXYZ", "revenue": 8500, "tier": "pro", "status": "trial"},
        {"id": "c003", "name": "BigBank LLC", "revenue": 450000, "tier": "enterprise", "status": "active"},
    ],
    "metrics": {
        "mrr": 583500,
        "churn_rate": 0.021,
        "new_customers_this_month": 12,
        "support_tickets_open": 47
    }
}


def query_customers(filter_tier: str = None, filter_status: str = None) -> list:
    customers = SAMPLE_BUSINESS_DATA["customers"]
    if filter_tier:
        customers = [c for c in customers if c["tier"] == filter_tier]
    if filter_status:
        customers = [c for c in customers if c["status"] == filter_status]
    return customers


def get_business_metrics() -> dict:
    return SAMPLE_BUSINESS_DATA["metrics"]


def get_customer_by_id(customer_id: str) -> dict | None:
    for c in SAMPLE_BUSINESS_DATA["customers"]:
        if c["id"] == customer_id:
            return c
    return None


# ============================================================
# MCP Server Definition
# ============================================================

app = Server("business-data-mcp")


@app.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """
    Declare all tools this MCP server provides.
    Claude reads these descriptions to know when to call each tool.
    """
    return [
        types.Tool(
            name="query_customers",
            description="""Query customer data. Use when asked about customers, accounts,
            or client information. Can filter by tier (free/pro/enterprise) or status (active/trial/churned).""",
            inputSchema={
                "type": "object",
                "properties": {
                    "filter_tier": {
                        "type": "string",
                        "enum": ["free", "pro", "enterprise"],
                        "description": "Filter customers by subscription tier"
                    },
                    "filter_status": {
                        "type": "string",
                        "enum": ["active", "trial", "churned"],
                        "description": "Filter customers by status"
                    }
                }
            }
        ),
        types.Tool(
            name="get_business_metrics",
            description="""Get current business metrics including MRR, churn rate, new customers,
            and support ticket counts. Use when asked about overall business performance.""",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        types.Tool(
            name="get_customer_by_id",
            description="Get detailed information about a specific customer by their ID.",
            inputSchema={
                "type": "object",
                "properties": {
                    "customer_id": {
                        "type": "string",
                        "description": "Customer ID (e.g., c001, c002)"
                    }
                },
                "required": ["customer_id"]
            }
        )
    ]


@app.call_tool()
async def handle_call_tool(name: str, arguments: dict[str, Any]) -> list[types.TextContent]:
    """Route tool calls to the right handler and return results."""

    if name == "query_customers":
        results = query_customers(
            filter_tier=arguments.get("filter_tier"),
            filter_status=arguments.get("filter_status")
        )
        return [types.TextContent(
            type="text",
            text=json.dumps(results, indent=2)
        )]

    elif name == "get_business_metrics":
        metrics = get_business_metrics()
        return [types.TextContent(
            type="text",
            text=json.dumps(metrics, indent=2)
        )]

    elif name == "get_customer_by_id":
        customer = get_customer_by_id(arguments["customer_id"])
        if customer is None:
            return [types.TextContent(type="text", text=f"No customer found with ID: {arguments['customer_id']}")]
        return [types.TextContent(
            type="text",
            text=json.dumps(customer, indent=2)
        )]

    else:
        raise ValueError(f"Unknown tool: {name}")


# ============================================================
# Optional: Resources (expose data as readable context)
# ============================================================

@app.list_resources()
async def handle_list_resources() -> list[types.Resource]:
    """Resources are like files Claude can read for context."""
    return [
        types.Resource(
            uri="business://overview",
            name="Business Overview",
            description="High-level overview of the business data available through this MCP server",
            mimeType="text/plain"
        )
    ]


@app.read_resource()
async def handle_read_resource(uri: str) -> str:
    if uri == "business://overview":
        return """Business Data MCP Server

Available tools:
- query_customers: Get customer list with optional filtering
- get_business_metrics: Current MRR, churn, growth metrics
- get_customer_by_id: Detailed customer lookup

Data freshness: Real-time (queries live database)
Access level: Read-only
"""
    raise ValueError(f"Unknown resource: {uri}")


# ============================================================
# Run the server
# ============================================================

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="business-data-mcp",
                server_version="0.1.0",
                capabilities=app.get_capabilities(
                    notification_options=None,
                    experimental_capabilities={}
                )
            )
        )


if __name__ == "__main__":
    asyncio.run(main())

"""
To connect this to Claude Code, add to your ~/.claude.json or project .claude/settings.json:

{
  "mcpServers": {
    "business-data": {
      "command": "python",
      "args": ["/path/to/05-mcp-server-skeleton.py"]
    }
  }
}

Then in Claude Code, you can ask:
  "How many enterprise customers do we have?"
  "What's our current MRR?"
  "Show me all trial customers"

Claude will automatically use the MCP tools to answer.

=== BUSINESS MODEL FOR MCP SERVERS ===

If you have valuable proprietary data or industry-specific tools,
you can package them as a managed MCP server and charge for access:

1. Host the MCP server as a cloud service (Railway, Fly.io, etc.)
2. Add authentication (API keys per customer)
3. Charge $X/month for access
4. Every developer building a Claude app that needs your data becomes a customer

Target: developers building Claude applications in your industry
Pricing: $50-500/month depending on data value and query volume

Examples:
- Real estate MLS data MCP: $99/month
- Medical literature MCP: $299/month
- Financial filings MCP: $199/month
- Shipping/logistics data MCP: $149/month
"""
