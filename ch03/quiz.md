## Q1

Which CC prompt is most useful for finding hidden weaknesses in your theoretical argument?

- [ ] "Summarize my hypothesis in one sentence."
- [x] "What assumptions am I making that I'm not explicitly stating?"
- [ ] "Give me three papers that support my hypothesis."
- [ ] "Write my hypothesis as a LaTeX equation."

> This prompt forces CC to surface the implicit premises in your argument — the things you've taken for granted that reviewers won't. It's the most direct route to the assumptions that could undermine your theory if left unexamined.

---

## Q2

CC generates a fully formatted citation — author names, year, journal, and title — that perfectly supports your argument. What do you do?

- [ ] Include it directly; CC's citations are usually accurate.
- [ ] Use it only in a draft, not the final version.
- [ ] Paraphrase the citation so it's harder to check.
- [x] Verify the full citation independently — title, authors, year, and journal — before including it anywhere.

> CC can confabulate plausible-looking but nonexistent citations. The author names, titles, and journal names it generates may be real in isolation but combined into a reference that doesn't exist. Always verify against Google Scholar, Semantic Scholar, or your field's primary database before using any CC-generated citation.

---

## Q3

You want to stress-test your hypothesis by considering alternative explanations. Which prompt works best?

- [ ] "Is my hypothesis correct?"
- [ ] "Find weaknesses in my methodology."
- [x] "Here is my hypothesis. Generate three alternative hypotheses that could explain the same data."
- [ ] "Summarize the literature on my topic."

> Generating rival hypotheses forces you to consider what a skeptic would argue and what evidence would distinguish your preferred explanation from the alternatives. It's a direct application of strong inference — identifying the observations that would rule out each competing account.

---

## Think

Describe a theoretical claim in your own research. How would you use the steelman technique with CC to stress-test it before writing it up?

<answer>
Start by stating the claim clearly in 2-3 sentences, then ask CC to steelman it: produce the most rigorous, defensible version of the argument, filling in implicit assumptions and sharpening the logic. Next, ask CC to attack the steelmanned version — identifying the three strongest counterarguments a skeptical reader would raise. Finally, for each counterargument, ask how you would design an analysis or study that would rule it out. The key insight is that you are stress-testing the strongest version of your argument, not a weak version — so the vulnerabilities CC surfaces are the ones that will actually matter to readers. Use the results to strengthen the argument where possible, and to explicitly acknowledge limitations where you cannot fully resolve the objection. This surfaces reviewer objections before submission rather than after.
</answer>
