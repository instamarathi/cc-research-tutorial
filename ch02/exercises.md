# Exercises: Simulations & Code

## Exercise 1: Write a Simulation from Scratch

**Time: ~20 minutes**

In this exercise you will prompt CC to write, run, and extend a simulation — without writing any code yourself.

**Setup:** Open CC in a new empty directory.

**The task:** Use the following simulation (or substitute one from your own research):

> Simulate N particles performing a 2D random walk. Each particle starts at the origin. At each step, each particle moves one unit in a randomly chosen direction (up, down, left, or right). After 500 steps, compute the straight-line distance of each particle from the origin. Run the simulation with 1000 particles and plot a histogram of the final distance distribution.

**Prompt CC with something like:**

```
Simulate 1000 particles doing a 2D random walk. Each particle starts at the
origin and takes 500 steps, moving one unit in a random cardinal direction
each step. After all steps, compute the Euclidean distance from the origin
for each particle. Plot a histogram of the final distances. Run the script
and show me the plot.
```

**Then extend it:** Once you have a working simulation, ask CC: "Add a command-line argument for the number of steps so I can run different configurations without editing the file."

**What to notice:** Did CC write the script, run it, and return the plot without you touching any code? How did it handle the extension request — did it remember the context from the first prompt?

---

## Exercise 2: Debug a Broken Script

**Time: ~15 minutes**

In this exercise you will give CC a script with multiple bugs and ask it to fix them by running the code.

**Setup:** Create a file called `buggy.py` in a new directory with this content:

```python
import numpy as np

def run_simulation(n_steps, n_particles):
    positions = np.zeros(n_particles)
    for step in range(n_steps):
        positions += np.random.choice([-1, 1], size=n_particls)  # typo
    return positions

results = run_simulation(100, 500)
print(f"Mean final position: {results.meen():.3f}")  # wrong method
```

This script has two bugs: a variable name typo (`n_particls`) and a wrong method name (`meen()` instead of `mean()`).

**Prompt CC:**

```
Run buggy.py. If it fails, fix all the errors and run it again until it
produces output.
```

**What to notice:** CC should find and fix both bugs in sequence. Watch how it handles the second error after fixing the first — does it continue the loop without being asked? Does it confirm the final output is reasonable?

---

## Exercise 3: Optimize an Existing Script

**Time: ~10 minutes**

In this exercise you will ask CC to profile a slow script and make it significantly faster.

**Setup:** Either use a slow script from your own work, or ask CC to create a deliberately slow simulation first: "Write a slow Python script that simulates 5000 particles doing a 1D random walk for 1000 steps using a Python for loop (not vectorized). Time it and print the elapsed time."

**Once you have a slow script, prompt CC:**

```
Profile this script and identify the bottleneck. Then rewrite the slow
part to be at least 5× faster. Show me the timing before and after so
I can verify the speedup.
```

**What to notice:** CC should use `cProfile` or `time` to measure performance, identify the loop or operation that dominates, and propose a vectorized numpy equivalent. Ask it to explain *why* the faster version is faster — this is a good way to learn numpy idioms while getting a working result.
