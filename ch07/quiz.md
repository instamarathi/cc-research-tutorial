# Quiz: Research Habits That Compound

## Q1

What is the primary purpose of a `CLAUDE.md` file in a research project?

- [ ] To document your code so other developers can understand it
- [x] To give CC persistent project context that survives across sessions
- [ ] To replace a README for your GitHub repository
- [ ] To store API keys and environment variables

> CLAUDE.md is read automatically by CC at session start. Its purpose is to load project context — research question, file structure, current status, conventions — so you do not have to re-explain these things each time. It is a briefing document for CC, not documentation for collaborators.

---

## Q2

Your CLAUDE.md has grown to 500 lines over a year of daily updates. What should you do?

- [ ] Leave it as is — more context is always better for CC
- [ ] Delete it and start fresh from scratch
- [ ] Move it to a `docs/` folder so it is out of the way
- [x] Review it, remove stale sections, and condense it to the most relevant context

> Long CLAUDE.md files waste context window space and can bury the most relevant information under outdated history. The right approach is a periodic review: remove sections describing completed work, condense session logs to key decisions and findings, and keep only what CC needs to orient itself today. A well-maintained 100-line CLAUDE.md outperforms a neglected 500-line one.

---

## Q3

What is the best way to start a CC session when you have a CLAUDE.md?

- [ ] "Here is my project context: [paste entire CLAUDE.md manually]"
- [ ] Just describe the task — CC will figure out the rest
- [x] "Read CLAUDE.md. What should I work on today based on the current status?"
- [ ] "Summarize the project for me before we start"

> CC reads CLAUDE.md automatically, but asking it to explicitly orient itself and connect the context to today's priorities produces better task recommendations. The prompt combines context retrieval ("Read CLAUDE.md") with a specific, actionable question ("What should I work on today?") — this grounds CC's response in your project's actual current state.

---

## Think

Describe what you would put in a `CLAUDE.md` for your current or most recent research project. Include at least four sections and explain why each one saves time in a CC session.

<answer>
Strong answers include four or more of these sections with explanations of their value:

(1) Research question or project goal — one sentence describing what the project is trying to find out or produce. This saves having to explain the project from scratch every session and prevents CC from giving generic suggestions disconnected from your actual aims.

(2) File structure — which directories contain what, which files are inputs versus outputs, which scripts do what. This saves CC from guessing where to look or accidentally modifying files it should not, and lets you ask questions like "what file should I open?" and get a useful answer.

(3) Current status — what is done, what is in progress, what is blocked. This is what lets you start a session with "what should I work on?" and receive a specific recommendation. Without it, CC cannot distinguish between a project that needs analysis and one that needs writing.

(4) Conventions and definitions — project-specific terminology, variable naming standards, date formats, style preferences. This prevents CC from using generic terminology that conflicts with your discipline or your collaborators' expectations, and ensures code and writing output is consistent with your existing work.

Bonus sections: a "Do not" list to prevent repeated mistakes; a key contacts or reference list; a bibliography of essential papers the project depends on. Full credit for any four sections with clear explanations of why each one reduces re-explanation overhead in a real session.
</answer>
