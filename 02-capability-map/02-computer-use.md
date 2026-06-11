# Computer Use — Automate Any GUI

## What It Is

Computer Use gives Claude a virtual desktop. Claude can:
- See screenshots of the screen
- Move the mouse to specific coordinates
- Click buttons, links, form fields
- Type text
- Scroll
- Take screenshots to see the result of its actions

This means Claude can operate **any software that has a GUI** — even software with no API.

---

## The Technical Loop

```
1. Claude receives screenshot of current screen state
2. Claude decides what action to take (click, type, scroll)
3. Claude outputs an action block: {"type": "mouse_move", "coordinate": [520, 340]}
4. Your code (or Anthropic's container) executes the action
5. New screenshot is taken and sent to Claude
6. Loop repeats until task is complete
```

### Tool Declaration

```python
tools = [
    {
        "type": "computer_20250124",
        "name": "computer",
        "display_width_px": 1280,
        "display_height_px": 800,
        "display_number": 1  # For multi-display setups
    },
    {
        "type": "text_editor_20250124",
        "name": "str_replace_editor"
    },
    {
        "type": "bash_20250124",
        "name": "bash"
    }
]
```

---

## Two Deployment Options

### Option 1: Self-Hosted
You provide:
- A virtual machine or container with a display (X11 or Wayland)
- Screenshot capture mechanism
- Mouse/keyboard input mechanism
- A way to send screenshots to Claude and receive actions

Anthropic provides:
- A Docker reference implementation: `ghcr.io/anthropics/anthropic-quickstarts:computer-use-demo-latest`
- This demo sets up the full loop for you

### Option 2: Managed Agents (Anthropic Hosts)
Add Computer Use as a skill in your Managed Agent configuration. Anthropic provides the container, display, screenshot capture, and action execution. You just get results.

---

## What Computer Use Can Do (And Can't)

### Can Do
- Fill out web forms on any website
- Navigate web applications without APIs
- Extract data from web pages by reading them visually
- Operate legacy desktop software (Excel, old CRM systems, etc.)
- Multi-step workflows spanning multiple applications
- Take actions based on what it sees (conditional logic)

### Current Limitations
- Slower than API-based automation (each action requires a screenshot round-trip)
- More expensive than scraping (many LLM calls per task)
- Not reliable enough for safety-critical actions without human oversight
- Some anti-bot measures detect automated browser control
- Claude sometimes makes mistakes navigating complex UIs

### Best Use Cases
- **Low-volume, high-value tasks** — Research tasks that would take a human 2 hours
- **Legacy system integration** — Old software that has no API but costs $500K to replace
- **Web research automation** — Navigate research sites that block scrapers
- **Demo/prototype** — Show stakeholders what automation could look like before building APIs

---

## The Business Case for Computer Use

### The Market It Targets

There are thousands of companies running critical operations on software that has:
- No public API
- Expensive/impossible integration costs
- IT departments that won't approve new integrations

Examples:
- Healthcare: Epic, Cerner medical record systems
- Legal: Westlaw, Lexis-Nexis research platforms
- Finance: Bloomberg Terminal, legacy banking systems
- Government: ancient agency systems that can't be replaced
- Small business: local accounting software, local POS systems

### The Business Opportunity

**"AI wrapper for legacy software"** — charge $X/month to automate workflows in software that has no API. The customer cannot get automation any other way. You become infrastructure.

Specific plays:
1. **Medical records automation** — Extract data from EHR systems for billing/analytics
2. **Legal research automation** — Run Westlaw/LexisNexis searches and synthesize results
3. **Government form submission** — Automate repetitive government portal interactions for businesses
4. **Competitor price monitoring** — Scrape competitor sites that block traditional scrapers
5. **QA testing automation** — Test web apps without instrumenting the code

---

## Cost Model for Computer Use

Computer Use is significantly more expensive than API calls because:
- Each action = one API call (screenshot + action decision)
- A typical 10-step task = 10+ API calls
- Screenshots add input tokens (image tokens = significant cost)

Budget: **$0.50 - $5.00 per complex task** on Opus 4.8

This means computer use products need to automate tasks worth $20+ in human time to have viable economics. Focus on high-value, infrequent tasks — not high-volume, low-value automation.
