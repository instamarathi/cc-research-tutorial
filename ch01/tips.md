# Tips for Research Sessions

## 1. Point CC to specific files rather than describing them

Instead of telling CC what your data looks like, let it read the file directly.

"Read data/survey.csv and describe its structure" gives CC the ground truth. Describing the file in prose introduces your own interpretation and wastes context tokens. Always prefer: `Read <path>`.

## 2. Ask CC to make a to-do list for your research session

When you sit down to work but are not sure where to start, try:

```
Given the files in this project, suggest 5 concrete tasks I could do today to move this research forward.
```

CC will generate a prioritized list based on what it can see. You decide which one to do first. This turns an unfocused morning into a structured session in about 30 seconds.

## 3. Use "explain like I just picked this up" for unfamiliar papers

If a paper is dense or outside your immediate area, ask:

```
Explain the core argument of this paper as if I just picked it up for the first time and have five minutes.
```

This sidesteps jargon and gets you to the logic quickly. You can then ask CC to go deeper on whichever part matters most for your work.

## 4. Ask CC to find contradictions between two papers

Comparing papers manually is slow. Give CC both texts and ask directly:

```
Read paper_a.txt and paper_b.txt. Where do they contradict each other, and where do they agree?
```

CC will surface the tensions. Your job is to decide which position is better supported — CC can help you think that through too, but the judgment is yours.

## 5. Save important CC outputs to a file

Anything CC produces that you want to keep needs to be written to disk, because the session does not persist.

Get into the habit of ending a productive exchange with:

```
Write your summary of this analysis to session-notes/2026-05-01.md
```

Use today's date in the filename. Over time these session notes become a searchable research log you can hand back to CC in future sessions.

## 6. Text-only formats work best — extract PDFs before starting

CC cannot read binary formats. Convert before you start, not mid-session:

```bash
pdftotext paper.pdf paper.txt          # single paper
for f in papers/*.pdf; do pdftotext "$f" "${f%.pdf}.txt"; done  # whole folder
```

Once converted, drop the `.txt` files into your project directory and CC can read as many as fit in its context window. For a literature review, converting your entire reading list upfront saves friction later.
