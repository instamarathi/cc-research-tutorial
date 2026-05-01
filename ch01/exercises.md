# Exercises

## Exercise 1: Analyze a Dataset

**Time: 15 minutes**

**What you need:** Any CSV file — survey data, experimental results, a public dataset you have downloaded, or even a spreadsheet exported from Excel.

**Steps:**

1. Open Claude Code in the directory where your CSV lives:
   ```bash
   claude
   ```

2. Ask CC to read and describe the file:
   ```
   Read mydata.csv. What is the structure — how many rows and columns, what are the column names, and are there any obvious data quality issues?
   ```

3. Follow up by asking for patterns:
   ```
   What are 3 interesting patterns or anomalies you notice in this data?
   ```

4. Ask CC to write a visualization script:
   ```
   Write a Python script using matplotlib to visualize the most interesting pattern you identified. Save the figure as figures/exploration.png.
   ```

5. Run the script:
   ```bash
   uv run python explore.py
   ```

**What to notice:** The progression from structure → patterns → code all happens in one conversation. Each step uses what CC already knows from the previous one.

---

## Exercise 2: Deep-Dive a Paper

**Time: 15 minutes**

**What you need:** One academic paper as a `.txt` file. If you only have a PDF, convert it first:
```bash
pdftotext your_paper.pdf your_paper.txt
```

**Steps:**

1. Start CC and orient it:
   ```
   Read your_paper.txt. What is the central research question and the key finding?
   ```

2. Dig into weaknesses:
   ```
   What are the 3 biggest limitations of this study? Be specific — point to the methods or data where each limitation originates.
   ```

3. Generate follow-up questions:
   ```
   If I wanted to build on this paper for my own research, what are 5 follow-up questions this paper leaves unanswered?
   ```

**What to notice:** You have moved from orientation to critique to research agenda in three prompts. This is faster than reading the paper top-to-bottom for the same outcome.

---

## Exercise 3: Compare Two Sources

**Time: 10 minutes**

**What you need:** Two short texts — two papers, a paper and a book chapter, two sets of notes, or two competing models described in prose. Convert to `.txt` if needed.

**Steps:**

1. Give CC both files at once:
   ```
   Read source_a.txt and source_b.txt.
   ```

2. Ask for agreement and disagreement:
   ```
   Where do these two sources agree, and where do they contradict each other? Give me a structured comparison.
   ```

3. Push deeper on one disagreement:
   ```
   Take the most significant contradiction you found. What evidence from each source supports its position?
   ```

**What to notice:** CC will organize the comparison in seconds. Crucially, your follow-up prompt forces it to go beyond surface-level differences and engage with the evidence — that is where the real analytical value lives.
