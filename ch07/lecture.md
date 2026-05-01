# Research Habits That Compound

## The Problem with One-Off Sessions

Most researchers start with CC the same way: open a terminal, paste in some data, fix a problem, close. The next day they open a new session and spend the first ten minutes re-explaining the project — what the variables mean, where the files live, what they were working on last time.

This is reactive use. CC is a powerful tool, but without context it is a blank slate every morning. You are doing extra work to compensate for its lack of memory, and that friction accumulates. Across a semester, those re-explanation minutes add up to hours.

The tools in this chapter change the relationship. They turn CC from a one-off assistant into a persistent research partner — one that knows your project, your conventions, and your current priorities every time you open a session.

## CLAUDE.md: Your Project's Memory

CC automatically reads a file called `CLAUDE.md` at the root of your project directory when a session starts. Whatever you put in that file, CC has before you say a single word. You do not have to ask it to read anything; the context is already loaded.

Think of `CLAUDE.md` as a briefing document you write for a very capable research assistant who has total amnesia between visits. Every time they arrive, they read the briefing and pick up exactly where they left off.

A good research `CLAUDE.md` contains six things:

- **Project name and research question** — one sentence. What is this project trying to find out?
- **Key concepts with precise definitions** — the terms CC might get wrong or interpret generically. If your project uses "flux" to mean something specific, say so.
- **File structure** — what is in each directory, what the key scripts do, and what outputs are intermediate versus final.
- **Current status** — what is done, what is in progress, what is blocked. This is what lets you start a session with "what should I work on?" and get a useful answer.
- **Conventions** — naming schemes, date formats, variable naming standards, style preferences.
- **Do not list** — common mistakes CC has made (or might make), files not to touch, commands not to run.

Here is a realistic example for an environmental science project:

```markdown
# Project: Carbon Flux Model

**Research question:** How does soil moisture interact with carbon efflux under drought conditions?

**Key files:**
- `data/raw/` — never modify; original flux tower measurements
- `data/processed/` — cleaned outputs; regenerate with `scripts/clean.py`
- `models/` — simulation scripts; main entry point is `run_model.py`

**Conventions:** All dates in ISO 8601. Variable names follow FLUXNET standard.

**Current status:** Data cleaning complete. Working on model calibration (see `TODO.md`).

**Do not:** Commit to `data/raw/`. Edit `requirements.txt` without testing.
```

Notice what this file does not contain: it does not reproduce the data, explain basic concepts, or document every function. It contains only what CC needs to orient itself — the things a new collaborator would need to know in the first five minutes.

> [!TIP]
> Keep CLAUDE.md under 200 lines. Long files waste context and slow down session start. If your CLAUDE.md is growing beyond that, condense the current-status section and move older log entries to a separate `CHANGELOG.md`.

> [!TRY]
> Navigate to a real research project directory right now and ask CC: "Look at the files in this directory. Write a CLAUDE.md that describes this project." Review what it produces — add anything it missed, remove anything inaccurate. You now have a working briefing document.

## Hooks: Automating Repetitive Context

For researchers who want to go further, CC supports hooks — shell commands that run automatically before or after CC actions. Hooks live in `.claude/settings.json` in your project directory.

Common uses in research workflows:

- **Before a session starts:** run `git status` so CC automatically knows which files have changed since your last commit.
- **After CC edits a script:** automatically run your test suite so failures surface immediately.
- **After CC writes output:** run a linting or formatting script to keep code consistent.

A hook entry looks like this:

```json
{
  "hooks": {
    "preToolUse": [
      {
        "matcher": "Bash",
        "hooks": [{ "type": "command", "command": "git status" }]
      }
    ]
  }
}
```

For most researchers, `CLAUDE.md` is sufficient and hooks are not necessary. Hooks are for advanced automation — when you have identified a repetitive manual step that happens in every session and is worth the setup time to eliminate. Start with `CLAUDE.md`, and only reach for hooks when you have a specific friction point that a hook would solve.

## Building a Workflow That Compounds

The value of these tools comes from using them consistently. Here is a weekly CC research routine that builds on itself over time:

**Monday:** Open `CLAUDE.md` directly and update it. Add what you finished last week to the completed section. Write this week's priorities into the current-status section. This takes five minutes and means every session this week starts oriented.

**Daily sessions:** Start with "Read CLAUDE.md. What should I work on today based on current status?" CC will give you a task recommendation grounded in your own priorities — not a generic suggestion.

**After analysis:** End substantive sessions with "Update the Current Status section of CLAUDE.md with what we just did." This closes the loop. The next session starts knowing what happened.

**Before writing:** "Read CLAUDE.md and style-guide.md. Let's draft the methods section." CC writes in your voice, using your conventions, with knowledge of your project's specific claims.

The compounding effect is real. After a month of this routine, your `CLAUDE.md` encodes hard-won project knowledge: which data files have quirks, which approaches you already tried, what your advisor thinks about the framing. CC does not rediscover this each session — it already knows.

> [!NOTE]
> The most productive CC users treat it as a collaborator, not a tool. Collaborators need context. Give CC context systematically and it returns that investment. A tool you have to re-explain every time is not saving you time; a collaborator who remembers is.
