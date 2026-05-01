# Exercises

## Exercise 1: AI Marker Hunt

**Time: 10 minutes**

Read this paragraph:

> "It is worth noting that the results of this study demonstrate a significant improvement in performance. Furthermore, the findings highlight the importance of considering multiple variables when conducting research. It can be seen that researchers who utilize these methods will achieve better outcomes. In conclusion, this approach is highly recommended for future studies in this area."

**Step 1: Before you open CC**, list every AI writing marker you can spot. Write them down. This builds your editorial eye independently of any tool.

**Step 2:** Ask CC to analyze it:

```
List every AI writing marker in this paragraph. For each one, say what it is and why it signals AI-generated prose.
```

Compare CC's list to yours. Note anything you missed.

**Step 3:** Ask CC to rewrite it:

```
Rewrite this paragraph eliminating all AI writing markers. Write in the voice of a specific, confident researcher who knows exactly what their data showed and is not hedging. Replace every vague phrase with a concrete claim.
```

Read the result. The rewrite should be shorter, more specific, and harder to have written without the underlying data.

---

## Exercise 2: Polish Your Own Writing

**Time: 15 minutes**

**What you need:** One paragraph from your own academic writing — a draft, a conference abstract, a manuscript section, anything.

**Steps:**

1. Paste the paragraph into a file and open CC on that directory.

2. Run Pass 1:
   ```
   Rewrite this paragraph removing all hollow filler transitions and empty openers. Do not add anything — only cut or replace dead phrases with the actual content they were obscuring.
   ```

3. Run Pass 2 on the result:
   ```
   Rewrite this passage varying sentence length deliberately. Some sentences under 10 words. Some over 25. The rhythm should feel controlled, not mechanical.
   ```

4. Run Pass 3 if you have a style guide. If not, skip to Pass 4.

5. **Read the final version aloud.** Mark anything that makes you stumble. Edit those by hand.

**What to notice:** The original and the final version will differ less than you expect — but the differences will be in exactly the right places.

---

## Exercise 3: Build Your Banned Phrases List

**Time: 10 minutes**

**Steps:**

1. Create the file:
   ```bash
   touch banned-phrases.md
   ```

2. Add the starter list plus at least 5 phrases specific to your own field or your own writing habits. Think about the phrases you use when you're uncertain, when you're padding, or when you're gesturing at a point rather than making it.

3. Test it on a sample paragraph — your own or the one from Exercise 1:
   ```
   Read banned-phrases.md. Remove every instance of these phrases from the following text. Where a phrase was hiding a real point, rewrite the sentence to state the point directly. Where it was empty, delete it.
   ```

4. Review each removal. For every deleted phrase, ask: was something actually being said there? If yes, make sure the rewrite says it. If no, the deletion is correct.

**What to notice:** The file becomes a permanent editorial tool. Add to it whenever you notice a recurring phrase that weakens your prose. Run it before submission, not just when you think you've used AI.
