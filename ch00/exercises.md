# Exercises: Welcome & The Superpower

## Exercise 1: Install and First Contact (10 min)

Get CC running and have your first real conversation with it.

**Steps:**

1. Confirm Node.js is installed: `node --version`. If it's missing, install it from [nodejs.org](https://nodejs.org) before continuing.
2. Install Claude Code: `npm install -g @anthropic-ai/claude-code`
3. Get your API key from [console.anthropic.com](https://console.anthropic.com) and set it: `export ANTHROPIC_API_KEY="your-key-here"`
4. Navigate to any folder on your machine that has some files in it — a project directory, a folder with scripts, even your Desktop.
5. Run `claude` to start a session.
6. Type the following prompt and press Enter:

   `List the files here and summarize what each one might be for.`

7. Read CC's response. Notice that it read your directory without you copying or pasting anything.

**What to observe:** CC should list the files and make reasonable guesses about their purpose based on names and content. This is the baseline capability — it knows where it is and what it can see.

---

## Exercise 2: Ask CC About Itself (5 min)

Understand what makes CC different from the chat AI you've used before.

**Steps:**

1. With CC still running from Exercise 1 (or start a new session with `claude`), ask:

   `What can you do that Claude.ai cannot?`

2. Read the answer carefully. CC should mention file access, shell commands, and iteration.
3. Then ask:

   `What tools do you have access to right now?`

4. CC will list its available tools — things like reading files, writing files, running bash commands, and searching the web (if enabled).

**What to observe:** Pay attention to the difference between "generating text" and "taking actions." The tools CC lists are capabilities that no chat interface can offer. This is the core of the mental model shift from the lecture.

---

## Exercise 3: The Context Test (10 min)

Experience first-hand how CC uses file context to give you better answers.

**Steps:**

1. Create a new folder and a text file inside it:

   ```bash
   mkdir test-project
   cd test-project
   ```

2. Using any text editor (or `nano notes.txt`), create a file called `notes.txt` with 3–4 sentences about a research idea or project you're currently thinking about. Write something real — the more genuine the content, the more useful CC's response will be.

3. Start CC from inside that folder:

   ```bash
   claude
   ```

4. Ask CC:

   `Read notes.txt and suggest three follow-up questions I should think about.`

5. CC will read the file and generate questions tailored to your actual content.

**What to observe:** CC didn't need you to paste the file contents. It read the file directly, understood the context, and gave you questions that are specific to what you wrote — not generic advice. Compare this to what you'd get from pasting the same text into Claude.ai. The answer might be similar, but notice that CC did the file-reading work for you, and could keep doing so across your entire project without any copy-pasting.
