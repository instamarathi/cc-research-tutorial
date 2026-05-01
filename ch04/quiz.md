## Q1

What is the biggest risk of asking CC to write an entire paper in a single prompt?

- [ ] CC will refuse to generate that much text.
- [ ] The writing will be too formal for academic journals.
- [x] Quality drops sharply and errors accumulate without review checkpoints.
- [ ] CC loses access to the file contents partway through.

> Without review checkpoints between sections, a wrong turn in the framing of one section propagates into everything that follows. By the time you read the output, you may have thousands of words built on a flawed premise — all of which need revision. Section-by-section drafting with approval between steps prevents this accumulation.

---

## Q2

You want CC to check whether your paper uses the same term consistently throughout. Which prompt works best?

- [ ] "Is my writing consistent?"
- [ ] "Edit this paper for clarity and precision."
- [x] "Scan the whole paper and flag any places where the same concept is referred to by different names or where terminology shifts."
- [ ] "Summarize each section of the paper."

> This prompt gives CC a specific, actionable task: find places where equivalent concepts are labeled differently. Vague prompts like "is my writing consistent?" invite a vague answer. Asking CC to quote the inconsistent passages directly produces output you can act on.

---

## Q3

You ask CC to draft your Introduction. What should you give CC before asking it to write?

- [ ] A list of all papers you plan to cite.
- [ ] The full text of a published Introduction from a similar paper.
- [ ] The word count you're targeting.
- [x] The paper's research question, main finding, and what the Introduction needs to accomplish.

> The Introduction's job is to set up the question and promise a contribution. CC can only write an Introduction that serves your specific paper if it knows what question you're answering, what you found, and what the section needs to do. Without this framing, CC will write a plausible-sounding Introduction for some paper — not necessarily yours.

---

## Think

A reviewer says your Discussion "overstates the generalizability of the findings." Describe a step-by-step process using CC to identify and fix the problem.

<answer>
Step 1: Ask CC to read both the Results section and the Discussion section to establish what the data actually shows versus what the Discussion claims. Step 2: Ask CC to identify every sentence in the Discussion that makes a claim about generalizability — quote each one. Step 3: For each flagged sentence, ask CC whether the data and analysis described in the Results section support that level of generalization, and why or why not. Step 4: For sentences that CC identifies as overclaiming, ask it to suggest a revised version with appropriate hedging — language that accurately represents the scope of the findings without abandoning the contribution. Step 5: Ask CC to check the revised Discussion as a whole: "Does any sentence in the revised Discussion still claim generalizability beyond what the Results support?" This final pass catches cases where the hedging in one sentence is undermined by the framing in an adjacent sentence. The result is a Discussion that makes its contribution clearly while accurately representing the limits of the study — which is also a better response to the reviewer than defensive hedging on every claim.
</answer>
