# Research Habits That Compound

## The Problem with One-Off Sessions

- **Reactive use** — open terminal, fix problem, close; repeat from scratch next time
- Every new session starts with 10 minutes of re-explaining the project
- CC is a blank slate without context — its memory resets completely between sessions
- Friction accumulates: re-explanation minutes across a semester add up to **hours**
- The tools in this chapter turn CC from a one-off assistant into a **persistent research partner**

## CLAUDE.md: Your Project's Memory

- CC **automatically reads `CLAUDE.md`** at project root when a session starts — no prompt needed
- Think of it as a briefing document for a capable assistant with total amnesia between visits
- Six things a research `CLAUDE.md` should contain:
  - **Project name and research question** — one sentence
  - **Key concepts** with precise definitions — terms CC might interpret generically
  - **File structure** — what lives where, what each script does, what outputs are final vs. intermediate
  - **Current status** — what's done, in progress, blocked
  - **Conventions** — naming schemes, date formats, style preferences
  - **Do not list** — common mistakes, files not to touch, commands not to run
- 💡 Keep `CLAUDE.md` under 200 lines — long files waste context; move older logs to `CHANGELOG.md`
- ⚡ Ask CC: "Look at this directory. Write a CLAUDE.md for this project." Review, correct, done.

## Example: CLAUDE.md for the Weather Project

```markdown
# Weather & Exercise Study
**Question:** Does bad weather reduce daily exercise?
**Data:** `weather_exercise/data/daily_steps.csv` — 50 people × 180 days
**Key vars:** `steps`, `precip_mm`, `temp_c`, `day_of_week`, `person_id`
**Always know:** rain effect ~28% step drop; temp effect smaller but significant
**Status:** analysis complete; drafting blog post "Why You Skip the Gym When It Rains"
**Do not touch:** `data/raw/` — use processed files in `data/` only
```

- **Project + question block** — one session start tells CC exactly what the project is for
- **Key vars line** — prevents CC from guessing column names or misreading the schema
- **Always know line** — seeds CC with the core finding so summaries stay consistent
- **Status line** — CC picks up where you left off without a re-explanation preamble

## Hooks: Automating Repetitive Context

- **Hooks** are shell commands that run automatically before or after CC actions
- Configured in **`.claude/settings.json`** in your project directory
- Common research uses:
  - Before session: run `git status` so CC knows which files changed
  - After CC edits a script: run your test suite automatically
  - After CC writes output: run a linter to keep code consistent
- Example hook entry runs `git status` before every Bash tool use:

```json
{
  "hooks": {
    "preToolUse": [
      { "matcher": "Bash",
        "hooks": [{ "type": "command", "command": "git status" }] }
    ]
  }
}
```

- **Start with `CLAUDE.md`** — reach for hooks only when you have a specific recurring friction point

## Example: Auto-Run Analysis on New Data

```json
{
  "hooks": {
    "postToolUse": [
      { "matcher": "Write",
        "hooks": [{ "type": "command",
          "command": "if echo '$CLAUDE_TOOL_OUTPUT' | grep -q 'data/.*\\.csv'; then uv run python analysis.py; fi" }] }
    ]
  }
}
```

- **Trigger on CSV writes:** any time CC writes a file matching `data/*.csv`, the analysis script re-runs automatically
- **Catches stale results:** without the hook, it's easy to edit raw data and forget to re-run — findings drift from the file on disk
- **uv run keeps deps locked:** the hook uses `uv run python` so the correct environment is always active, not whatever `python` resolves to
- **Low friction, high reliability:** one config change eliminates a manual step that's easy to skip under deadline pressure

## Building a Workflow That Compounds

- **Monday:** Update `CLAUDE.md` — move last week's work to completed, write this week's priorities (5 min)
- **Daily start:** "Read CLAUDE.md. What should I work on today?" — task recommendation grounded in your own priorities
- **After analysis:** "Update the Current Status section of CLAUDE.md with what we just did." — closes the loop
- **Before writing:** "Read CLAUDE.md and style-guide.md. Let's draft the methods section." — CC writes in your voice
- After a month, `CLAUDE.md` encodes **hard-won project knowledge**: data quirks, failed approaches, advisor framing
- 💡 Treat CC as a collaborator, not a tool — collaborators need context, and context compounds
