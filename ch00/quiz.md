## Q1

When you start `claude` in your terminal, what does it use as its primary context?

- [ ] Your Claude.ai chat history
- [ ] A project description you type at startup
- [x] Your current working directory and the files in it
- [ ] The last file you opened in your editor

> Claude Code reads your current working directory when it starts. This is why you should always launch it from inside your project folder — it's what gives CC its file awareness.

---

## Q2

Which of the following tasks can Claude Code do that Claude.ai cannot?

- [ ] Write a Python function that sorts a list
- [ ] Explain what a regular expression does
- [x] Run a shell command and read the output to decide what to do next
- [ ] Summarize a paragraph of text you paste in

> CC has tool use: it can execute shell commands, observe the output, and take the next action based on what it sees. Claude.ai only generates text in response to what you type — it cannot run anything or observe results.

---

## Q3

You want CC to help you debug a function in `analysis/preprocess.py`. What is the best way to give it context?

- [ ] Paste the entire file contents into the chat
- [ ] Describe the function from memory
- [ ] Paste just the broken function and ask what's wrong
- [x] Tell CC the filename and ask it to read it

> Telling CC to "read `analysis/preprocess.py`" lets it open the actual file in your project, see its imports and surrounding code, and give you a much more accurate answer than if you paste an isolated snippet. This is one of CC's core advantages.

---

## Think

Think back to the last time you used Claude.ai or ChatGPT for a coding or writing task. Describe one specific frustration with the copy-paste workflow, and explain how Claude Code would have changed that experience.

<answer>
Common frustrations include: losing all context when you close the tab and having to re-explain the project from scratch in the next session; having to manually copy error messages back into the chat after each failed run; not being able to reference multiple files at once without pasting them all in; the AI giving advice that doesn't fit your actual codebase because it can only see one snippet at a time; and the tedium of shuttling code back and forth between the editor and the browser. Claude Code addresses all of these: it persists context within a session, can read any file directly, runs code and sees the output itself, and operates across your whole project rather than on isolated pastes.
</answer>
