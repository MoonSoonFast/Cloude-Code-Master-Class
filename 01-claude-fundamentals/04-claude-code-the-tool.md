# Claude Code — The Development Tool

## What Claude Code Is

Claude Code is Anthropic's official CLI tool for software development. It is:
- A terminal-based coding agent you install on your machine
- An IDE extension for VS Code and JetBrains
- A reference implementation of how to build a Claude-powered coding agent

Critically: **Claude Code is built on the Claude API**. Everything it does is possible for you to replicate or extend. Understanding Claude Code helps you understand what's possible with Claude in development contexts.

---

## Key Capabilities

### Agentic Code Editing
- Reads and writes files directly
- Executes shell commands
- Runs tests and interprets results
- Commits to git
- Creates pull requests

Unlike a chat assistant that gives you code to paste, Claude Code acts directly on your codebase.

### MCP Server Support
Claude Code can connect to any MCP server, giving it access to:
- GitHub (repository operations)
- Databases (query your dev database directly)
- Internal tools (any MCP server you build)
- Third-party services (Slack, Linear, etc.)

### Hooks System
You can configure Claude Code to run shell commands before/after specific events:
- Before file writes
- After test runs
- On commit
- On tool use

This enables: automated formatting, test enforcement, security scanning, custom logging.

### Slash Commands
Custom commands you define in `.claude/commands/`:
```bash
# .claude/commands/review.md
Review the current diff for:
1. Security vulnerabilities
2. Performance issues  
3. Missing error handling
4. Test coverage gaps
```

Then invoke: `/review` and Claude Code runs your custom analysis.

### CLAUDE.md: Project Intelligence
Create `.claude/CLAUDE.md` in your project to give Claude persistent context:
```markdown
# Project: Payment Processing API

## Architecture
- FastAPI backend, PostgreSQL, Redis cache
- Payments via Stripe, payouts via Wise
- All financial operations require double-entry accounting

## Code Standards
- All database operations must use transactions
- Financial amounts always in integer cents, never float
- Every API endpoint requires authentication

## Test Requirements
- New payment flows need both unit and integration tests
- Use factory_boy for test data creation
```

Claude reads this on every session. It's the difference between Claude that understands your project and Claude that doesn't.

---

## Claude Code for Business Builders

### Competitive Advantage as a Solo Developer

Claude Code effectively gives a solo developer the output capacity of a small team. With it you can:
- Build MVPs in days, not weeks
- Maintain codebases larger than one person could normally handle
- Execute refactors that would be too risky to do manually
- Write comprehensive tests without spending days on them

This directly affects your ability to execute the business opportunities in Module 3.

### Using Claude Code to Build Your Product

For the competitive intelligence agent (Exercise 4), Claude Code helps:
- Scaffold the entire project structure
- Write and debug the tool execution loop
- Set up the scheduling mechanism
- Write tests for your tool implementations
- Handle API error cases you didn't think of

The workflow:
1. Describe the feature in plain English
2. Claude Code writes the code
3. You review and correct
4. Claude Code runs the tests
5. Iterate until it works

### Claude Code in the Product You're Building

Many Claude-powered products benefit from embedding Claude Code-like capabilities:
- Coding assistant features in dev tools
- Automated code review in CI/CD pipelines
- Documentation generation from codebases
- Automated bug triage and fix suggestion

If you're building for a technical audience, look at what Claude Code does and ask: "What subset of this would my target user pay for as a product?"

---

## Configuration Reference

### Global Settings (`~/.claude.json`)
```json
{
  "model": "claude-opus-4-8",
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {"GITHUB_TOKEN": "ghp_..."}
    }
  },
  "theme": "dark"
}
```

### Project Settings (`.claude/settings.json`)
```json
{
  "model": "claude-opus-4-8",
  "allowedTools": ["Read", "Write", "Bash", "Edit"],
  "mcpServers": {
    "project-db": {
      "command": "python",
      "args": ["./scripts/mcp-server.py"],
      "env": {"DATABASE_URL": "postgresql://localhost/mydb"}
    }
  }
}
```

### Hooks (`.claude/settings.json`)
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {"type": "command", "command": "black $CLAUDE_TOOL_OUTPUT_FILE"}
        ]
      }
    ]
  }
}
```

---

## Business Opportunities Specific to Claude Code

### Building on Top of Claude Code

The Claude Code agentic loop (read files, write files, run commands, iterate) is a powerful pattern. You can build products using the same architecture:

1. **AI code review service** — Claude Code-style analysis as a PR bot
2. **Automated technical documentation** — Analyze codebase → generate/update docs
3. **Security audit tool** — Scan codebase for vulnerabilities with deep understanding
4. **Database migration assistant** — Read schema, understand business logic, write safe migrations
5. **Test generation service** — Analyze untested code, generate tests in the project's style

These are all productizations of the Claude Code pattern applied to specific high-value workflows.
