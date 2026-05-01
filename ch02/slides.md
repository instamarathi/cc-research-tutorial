# Simulations & Code

## CC as Your Coding Partner

- Old workflow: write → run → copy error → paste into Claude.ai → fix → repeat
- **CC eliminates the copy-paste loop** — it reads your files, runs code, and sees full tracebacks directly
- CC can try a fix and immediately re-run to confirm — all in one turn
- Your role shifts: from **debugging syntax** to **evaluating whether the science is right**
- New workflow: describe the simulation → CC writes, runs, fixes → you review output
- ⚡ Try: ask CC to read a script and describe what each function does — no copy-pasting required

## Writing New Simulation Code

- Don't describe **implementation** — describe the **science**
- Think: "what would I tell a new PhD student who knows Python but not my subfield?"
- A good prompt covers: the **process**, the **parameters** (with ranges), the **expected output**, and asks CC to run it
- Example: "Simulate 1000 random walks of 100 steps. Plot a histogram of final positions. Run it."
- Vague science prompt beats precise numpy prompt — CC chooses the right implementation
- 💡 "Simulate 10,000 random walks and plot the distribution" > "initialize a 2D array and use cumsum"

## Example: Generating the Dataset

- **Prompt used:** "Write `simulate_data.py` that generates 50 people × 180 days of synthetic step/weather data. Columns: date, person_id, steps, temp_c, precipitation_mm. Steps should correlate negatively with rain. Save to `weather_exercise/data/daily_steps.csv`."
- CC writes the full script, runs it, and confirms the CSV exists — no copy-pasting
- Key generation logic — steps decrease on rainy days, with individual variation:

```python
rain = np.random.binomial(1, 0.3, n_days)
steps = 8000 + 40 * temp_c - 1500 * rain
steps += np.random.normal(0, 1200, n_days)  # person noise
```

- CC automatically seeds `np.random` for **reproducibility** — ask if it doesn't
- After generation: "Read `daily_steps.csv` and show me summary statistics" — quick sanity check
- If the correlation looks wrong, say "rain days show fewer steps on average, but not by much — why?" and CC will diagnose

## The Debug Loop

- Skip manual error reading — ask CC to run the script directly
- CC sees **full traceback + source code simultaneously** — no context lost
- Most effective prompt: `"Run simulate.py. If it fails, fix the error and run it again. Keep going until it produces output."`
- Works in one or two iterations for common errors (name errors, shape mismatches, missing imports)
- CC **verifies its own fix** by re-running — not just reasoning abstractly
- ⚠️ Be specific about "working": "The mean should be near 0, std near 10" beats "make it not crash"

## Iterative Improvement

- CC **retains full context** from the session — no need to re-explain the simulation
- **Speed**: "This takes 90 seconds. Profile it and make it 3× faster."
- **Progress**: "Add a progress bar that updates every 1000 iterations."
- **Parameterization**: "Replace hardcoded numbers with command-line arguments."
- **Refactoring**: "Refactor into a class for multiple runs with different parameter sets."
- **Validation**: "Add assertions that the output is statistically reasonable."
- Ask CC to show profile output before and after to verify speedups are real

## Running and Visualizing Results

- Ask CC to save results and generate plots in the **same session**
- Example: "Save results to `results.csv` and save the plot as `distribution.png`."
- Ask CC to **interpret the output**: "Does this distribution look like what we'd expect from a random walk?"
- If CC's description doesn't match your expectation — something is wrong with code or mental model
- Visualization defaults: **matplotlib** (standard), **seaborn** (statistical), **plotly** (interactive)
- Practical pattern: **run → save → describe** turns a black-box script into shared reasoning

## Example: Running the Analysis

- **Prompt 1:** "Write `analysis.py` that loads `daily_steps.csv`, makes a scatter plot of `temp_c` vs `steps`, saves it as `temp_vs_steps.png`."
- **Prompt 2:** "Add a rain-day comparison: box plots of steps on rain vs non-rain days. Save as `rain_comparison.png`."
- **Prompt 3:** "Add a simple OLS regression of steps on temp_c and a rain dummy. Print the summary table."
- Core regression block CC produces:

```python
X = sm.add_constant(df[["temp_c", "rain"]])
model = sm.OLS(df["steps"], X).fit()
print(model.summary())
```

- Ask CC to **interpret the output**: "The rain coefficient is −1 423. Is that a meaningful effect given average step counts?"
- If a plot looks off, paste the description — CC diagnoses without needing you to re-upload the image
