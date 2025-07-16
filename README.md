# 🧩 Rubik's Race Solver

This project was created for the CS246 Artificial Intelligence course at the American University of Armenia.

The goal is to solve the puzzle from the board game Rubik’s Race using classical AI search algorithms and compare their performance on scrambled puzzles of different difficulty levels.


## What This Project Does

- Represents the Rubik’s Race board as a 5x5 grid.
- Defines a goal region (the center 3×3 part of the board).
- Randomly scrambles the board by a certain number of valid moves.
- Tries to solve the puzzle using four search algorithms:
  - **A*** (A-Star Search)
  - **IDA*** (Iterative Deepening A-Star)
  - **Breadth-First Search (BFS)**
  - **Hill Climbing** (a local search method)

Each algorithm is compared based on:
- Whether it finds a solution.
- How many nodes it expands to reach the goal.

## How to Run

### 1. Install requirements

Only one external library is needed:

```bash
pip install pandas
```

### 2. Run a single puzzle test

To generate a random puzzle and solve it using all algorithms:

```bash
python main.py
```

### 3. Run the experiment

To reproduce the experiments described in the paper:

```bash
python experiment.py
```

This will:

- Run the algorithms on puzzles scrambled with different difficulty levels.

- Record the number of nodes expanded.

- Save the results to a CSV file called `experiment_results.csv`.

You can change how many puzzles to run and how difficult they are by modifying values in the script.


## About the Puzzle

Rubik’s Race is a sliding tile puzzle played on a 5×5 grid. One tile space is blank (`_`) and tiles can slide into it. The goal is to move tiles so that the center 3×3 window matches a target goal pattern.

This project treats it like a variation of the **N-Puzzle** and applies search algorithms to find a solution path from the scrambled board back to the goal.



## Experiment Summary

The `rubiks-race-solver-analysis.pdf` file included in this repository contains the full experimental results and analysis.

### Key Findings

- **IDA\*** with both **Manhattan Distance** and **Number of Misplaced Tiles** heuristics is the most efficient algorithm, expanding the fewest nodes overall.
- **BFS** works but is highly inefficient, expanding thousands of nodes.
- **Hill Climbing** is fast when it succeeds, but often fails due to local minima.
- **A\*** finds optimal paths but uses more memory and expands more nodes compared to IDA\*.
- The **distance from the goal** (i.e. number of scrambling steps) affects puzzle difficulty more than the board size itself.
