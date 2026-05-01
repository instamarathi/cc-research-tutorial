## Q1

You want to analyze a PDF paper with Claude Code. What is the first step?

- [ ] Drag the PDF into the terminal window
- [ ] Copy and paste the text from the PDF manually
- [x] Run `pdftotext paper.pdf paper.txt`, then tell CC to read the `.txt` file
- [ ] Ask CC to open the PDF directly with `Read paper.pdf`

> CC cannot read binary PDF files. You must extract the text first with `pdftotext`, then point CC to the resulting `.txt` file. Pasting manually works but loses formatting and is tedious for long papers.

---

## Q2

CC gives you a numerical result — for example, "the mean response time is 4.7 seconds" — but the number seems too high based on your intuition. What should you do?

- [ ] Trust CC — it does not make arithmetic errors
- [ ] Discard the entire analysis and start over
- [x] Tell CC you think the number is wrong, ask it to re-check, and verify the result independently
- [ ] Average CC's answer with your intuition

> CC can and does make arithmetic mistakes. The right response is to challenge it directly ("I don't think that's right — show me the calculation step by step") and independently verify with a quick script or manual check before using the number in your work.

---

## Q3

You open CC with a new dataset and want to start exploring. Which prompt will be most effective?

- [ ] "I have a survey dataset. What can you tell me about it?"
- [ ] "Analyze my data thoroughly."
- [x] "Read data/responses.csv. What is the structure and what are three interesting patterns?"
- [ ] "Tell me what questions I should ask about my dataset."

> The best first prompt is specific and actionable: it names the exact file, asks for structure (orientation), and asks for patterns (substance). Vague prompts like "analyze my data" force CC to guess what you want, often producing generic output that misses what actually matters for your research.

---

## Think

You are starting a literature review session with 5 papers, each already extracted to a `.txt` file. Describe the first 3 prompts you would send to CC and explain what you expect to get from each one.

<answer>
1. **"Read paper1.txt through paper5.txt. Give me a one-paragraph summary of each."**
   Expected output: a brief orientation to each paper — key argument, method, finding. This establishes a shared frame of reference so CC can reason across the papers in later prompts.

2. **"Which two of these papers are most closely related in their methodology? What do they share?"**
   Expected output: CC identifies a methodological cluster. This tells you where the literature has converged and gives you a starting point for synthesis. It also surfaces hidden connections you might have missed reading the papers independently.

3. **"Draft a 3-paragraph synthesis of the common themes across all five papers. Focus on what they collectively argue, not on summarizing each one individually."**
   Expected output: a first draft of the synthesis section. It will not be perfect — CC may over-generalize or miss nuance — but it gives you something to edit, which is faster than writing from a blank page.
</answer>
