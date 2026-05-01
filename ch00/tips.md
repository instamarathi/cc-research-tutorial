# Practical Tips for Chapter 00

## 1. Open Every Session With a One-Liner Context

Before asking CC to do anything, give it a single sentence about your project and today's goal: "I'm working on a finite-element solver for heat diffusion. Today I want to add adaptive time-stepping." This takes five seconds and prevents CC from making assumptions about your codebase. The more specific you are upfront, the less you'll need to correct it later.

## 2. Use `claude --continue` to Resume Where You Left Off

When you close a CC session and come back later, `claude --continue` picks up your most recent conversation. You won't have to re-explain your project or re-establish context — CC will remember what files it read, what changes it made, and what you were working on. This is especially useful for multi-day tasks.

## 3. `/help` Shows All Available Slash Commands

Type `/help` at any point inside CC to see the full list of built-in slash commands. These include things like `/clear` (reset the conversation), `/cost` (check token usage), and `/model` (switch models). You don't need to memorize them — just remember that `/help` is always there.

## 4. Say "Read file.py" Instead of Pasting Code

CC can read files directly from your project. If you paste code into the prompt, CC sees it as isolated text with no connection to the rest of your codebase. If you say "read `models/base.py`", CC opens the actual file, sees its imports, understands its context, and gives you much better answers. The rule: never paste code you can just name.

> [!TIP]
> You can also say things like "look at all the files in the `tests/` folder" or "read the last 50 lines of `output.log`". CC understands natural-language file references — you don't need to give exact paths every time.

## 5. Ctrl+C Stops Any Running Action Immediately

If CC starts doing something you didn't intend — running a long command, writing to the wrong file, going down the wrong path — press **Ctrl+C** immediately. This stops the current action without exiting CC. You can then clarify and continue. It is your most important safety control.

## 6. `/cost` Shows Token Usage for the Session

Type `/cost` at any time to see how many tokens the current session has used and what it has cost. This is useful for longer research sessions where CC reads many large files or runs many iterations. If you're watching your API spend, checking `/cost` periodically keeps you from surprises.
