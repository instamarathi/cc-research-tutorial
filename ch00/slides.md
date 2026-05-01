# Welcome & The Superpower

## The Copy-Paste Trap

- Chat AI sees only what you **paste** — one file at a time, stripped of dependencies
- Every new session starts at **absolute zero** — close the tab and context is gone
- You carry errors back manually: run, crash, copy traceback, re-explain, repeat
- The AI has never seen your **actual data**, your file structure, or your imports
- Real projects span dozens of files — **copy-paste AI is constitutionally blind** to this
- You have been using a calculator when you needed a computer

## Example: The Weather Project

- You have a CSV of 50 people's daily steps, temperature, and rainfall — you want to know if bad weather kills exercise habits
- **The copy-paste approach:** open a chat window, paste 20 rows, ask "is there a correlation?" — but the AI has no idea what the columns mean
- Every session: re-explain that `temp_c` is Celsius, `precipitation_mm` is daily rainfall, `steps` is the outcome — **30 seconds of throat-clearing every time**
- You paste a subset to fit the context window — the AI draws conclusions from **200 rows out of 9,000**
- You get an insight, close the tab, open a new one — and the AI has **no memory of what it found last time**
- With CC: `claude` from inside `weather_exercise/`, point it at the CSV once — it reads all 9,000 rows and remembers the schema for the whole session

## What Claude Code Changes

- CC is a **command-line agent** — not a chat interface, lives inside your terminal and project
- Has **tool use**: reads files, writes files, runs shell commands, observes output
- Doesn't just generate text — it **takes actions and responds to results**
- Like a collaborator at your screen: sees the same files, runs the code, reads the error
- Ask it to debug a 400-line script, run tests until they pass, or summarize three PDFs
- The **friction that made AI feel like a novelty** disappears

## Installation

- Prerequisite: **Node.js** installed (`node --version` to check; get LTS from nodejs.org)

```bash
npm install -g @anthropic-ai/claude-code
claude
```

- First launch prompts for your **Anthropic API key** — get one at console.anthropic.com
- Persist the key so you don't set it every session:

```bash
export ANTHROPIC_API_KEY="your-key-here"  # add to ~/.zshrc or ~/.bashrc
```

- 💡 Run `source ~/.zshrc` after editing your profile to apply immediately

## Your First 5 Minutes

- Always launch from **inside your project directory** — that's CC's primary context
- Three things to do at the start of every session (takes 30 seconds):
  - **Give context** — one sentence about the project
  - **State your goal** — what you want to accomplish today
  - **Describe constraints** — Python version, no new deps, etc.
- ⚡ Try it: run `claude`, then ask *"What files are in this directory and what might each be for?"* — no copy-paste required
- Example 3-part context setup for the weather project:
  - **Project:** "This is a dataset of daily steps, temperature, and rainfall for 50 people over 180 days."
  - **Goal:** "Today I want to find out whether precipitation days have significantly lower step counts."
  - **Constraints:** "Use only the standard library plus pandas and matplotlib — no new installs."
- Exit anytime with **Ctrl+C**

## The Mental Model Shift

- **Before CC:** AI generates code snippets you paste into your project
- **After CC:** AI partner working **inside your project** with you
- Generation = one-shot transaction — ask, get, implement, AI forgets
- Collaboration = **ongoing** — AI sees what you see, runs experiments, adjusts on results
- Unit of work shifts from **"a function"** to **"a task"**
- You are no longer limited by the size of your clipboard
