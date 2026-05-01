# Welcome & The Superpower

## The Copy-Paste Trap

If you've used Claude.ai or ChatGPT to help with research code, you already know the ritual. You write a prompt, paste your function, get back something that looks right, copy it into your editor, run it, watch it crash, copy the traceback, paste it back into the chat window, explain again what you were originally trying to do, get another snippet, repeat. On a good day you solve the problem in twenty minutes. On a bad day you spend an hour re-explaining context the AI has completely forgotten.

This is the **copy-paste trap**, and it has a hidden cost that compounds every session. The chat window has no idea what files are in your project. It has never seen your actual data. It doesn't know that `run_simulation.py` imports a custom class from `models/base.py`. Each new session starts at absolute zero. You are not iterating with a collaborator — you are repeatedly interviewing a stranger and then manually implementing their suggestions yourself.

What gets lost along the way:

- **File context.** The AI sees only what you paste. One file at a time, stripped of its dependencies.
- **Memory.** Close the tab and everything is gone. Reopen it and you are starting over.
- **Iteration.** You run the code. You see the error. But the AI doesn't — so you have to carry that information back manually, character by character.
- **The full picture.** Real research projects span dozens of files. Copy-paste AI is constitutionally blind to this.

You have been using a calculator when you needed a computer.

## What Claude Code Changes

Claude Code (CC) is not a chat interface. It is a command-line agent that lives inside your terminal, inside your project, with full access to your filesystem and shell. When you run `claude` in your project directory, it can read any file, execute any command, observe the output, and decide what to do next — without you copying anything.

> [!NOTE]
> CC is not ChatGPT in a terminal. The fundamental difference is **tool use**: CC has the ability to read files, write files, run shell commands, and observe their output. It doesn't just generate text — it takes actions and responds to results. This is what makes real iteration possible, not just conversation.

Think of it this way: the copy-paste workflow is like calling a consultant on the phone and reading your codebase to them line by line. Claude Code is a brilliant collaborator sitting next to you, looking at the same screen. You say "that function is broken" and they can see exactly which function, read the whole file, run it, read the error, and start fixing — all without you doing anything except watching and approving.

This changes what's possible. You can ask CC to read a 400-line simulation script and identify the bug. You can ask it to run your tests and keep iterating until they pass. You can ask it to read three papers you've saved as PDFs and summarize the methodological differences. The friction that made AI feel like a novelty disappears.

## Installation

Before installing Claude Code, make sure you have **Node.js** installed. You can check with:

```bash
node --version
```

If you don't have it, install it from [nodejs.org](https://nodejs.org) (LTS version recommended).

Then install Claude Code globally:

```bash
npm install -g @anthropic-ai/claude-code
claude
```

On first launch, CC will prompt you for your Anthropic API key. Get one from [console.anthropic.com](https://console.anthropic.com) — create an account, navigate to **API Keys**, and generate a new key. You can also set it as an environment variable in your shell profile:

```bash
export ANTHROPIC_API_KEY="your-key-here"
```

> [!TIP]
> Add `export ANTHROPIC_API_KEY="your-key-here"` to your `~/.bashrc` or `~/.zshrc` so you don't have to set it in every new terminal session. Run `source ~/.zshrc` (or `~/.bashrc`) afterward to apply it immediately.

## Your First 5 Minutes

Start CC by navigating to your project directory and running `claude`. This is important — CC uses your current working directory as its primary context.

> [!WARN]
> Always launch Claude Code from **inside your project directory**. If you run `claude` from your home directory or a random location, it won't know what project you're working on, and you'll lose the biggest advantage it has over chat-based AI.

Once CC starts, you'll see an interactive prompt. Three things to do in every new session:

1. **Give context.** Tell CC what the project is. One sentence is enough: "I'm working on a Python package that runs agent-based simulations of epidemic spreading."
2. **State your goal.** What do you want to accomplish today? "Today I want to fix the bug in the network initialization code."
3. **Describe constraints.** Any relevant limitations: "The code needs to run on Python 3.10 and can't use any new dependencies."

These three things take 30 seconds and save you from 20 minutes of re-explanation later.

To end a session, press **Ctrl+C**. CC will stop whatever it's doing immediately.

> [!TRY]
> Open your terminal, navigate to any folder that has some files in it, and run `claude`. Once it starts, type:
>
> `What files are in this directory? Give me a brief guess about what each one might be used for.`
>
> Watch CC read the directory and respond without you copying or pasting anything. Notice that you never had to tell it where to look — it already knows.

## The Mental Model Shift

Here is the before and after that matters most.

**Before Claude Code:** "I use AI to generate code snippets that I paste into my project."

**After Claude Code:** "I have an AI partner who is working inside my project with me."

This is not a small difference. Generation is a one-shot transaction — you ask, you get, you implement, the AI forgets. Collaboration is ongoing — the AI sees what you see, remembers what happened earlier in the session, can run experiments itself, and adjusts based on results.

For researchers, this means the unit of AI-assisted work shifts from "a function" to "a task." Instead of asking for a sorting algorithm, you ask CC to profile your simulation, identify the bottleneck, and optimize it. Instead of pasting in a paragraph for feedback, you ask CC to read the full section, check that it's consistent with your methods, and suggest revisions. The scope of what you can delegate expands dramatically.

The copy-paste workflow trained you to think in small, self-contained requests because that was all the medium could handle. CC removes that constraint. You are not limited by the size of your clipboard anymore.
