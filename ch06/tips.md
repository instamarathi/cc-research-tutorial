# Tips for Post-Writing Polish

## 1. The "read aloud" test beats all AI checks

After any polish pass, read the text out loud. A sentence can survive visual proofreading and collapse the moment you say it. Stumbling is a signal. If you have to re-read a sentence to get through it, your reader will too. Fix those by hand — no prompt required.

## 2. Ask CC to find the single worst sentence

Before you run the full polish workflow, ask:

```
Which single sentence in this passage is most obviously AI-generated? Why?
```

CC will identify the offender and explain what marks it. Reading that explanation teaches you to recognize the same pattern on your own. Over time this builds a personal editorial eye faster than any style guide.

## 3. Add your own banned phrases

The starter `banned-phrases.md` list covers common AI markers. Your field adds more. Computational social science has its "leveraging big data to unpack complex phenomena." Qualitative research has its "rich, thick description." Neuroscience has its "sheds light on the neural underpinnings of."

Every time you notice one, add it to the file. The list gets more useful the longer you work with it.

## 4. Polish in passes, not in one go

Each pass has one job. If you combine them — "remove hollow transitions and vary sentence length and apply the style guide" — you get mediocre results on all three. CC will trade off between goals rather than optimizing each one. One pass, one job, in sequence.

## 5. Preserve intentional stylistic choices

CC will smooth out deliberate choices along with accidental ones. If you want to keep a sentence fragment, an unconventional comma, or an abrupt transition that is doing rhetorical work, say so before the pass:

```
Keep the fragment in the second sentence — it's intentional. Polish everything else.
```

CC will respect an explicit instruction. It will not guess that a stylistic irregularity is intentional.

## 6. Ask for before/after with changes highlighted

After any polish pass, ask CC to show its work:

```
Show the original passage and your revision side by side, with each change marked.
```

This makes it easy to catch over-editing — places where CC changed something that was already good, or where the revision introduces a new problem. You review a diff, not a rewrite.
