# Rubik's Race Game Solver

This project is an AI-powered solver for the Rubik's Race game. It explores various artificial intelligence algorithms to efficiently solve the game, a modified version of the classic N-Puzzle problem. The goal is to achieve a target pattern on a grid, given a randomized starting state.

## Features

- Implements **informed** and **uninformed** search strategies.
- Algorithms included:
  - A* (with Manhattan Distance and Number of Misplaced Tiles heuristics)
  - Iterative Deepening A*
  - Hill Climbing
  - Breadth-First Search (for comparison)
- Comparative analysis of algorithm performance.

## Requirements

- Python 3.x

## How to Use

1. Clone the repository and navigate to the project directory.
2. Navigate to the `src` folder where the code files are located.
3. Run the main script `rubiks_race_solver.py`:
   ```bash
   python src/rubiks_race_solver.py
   ```
4. Customize grid size and initial states in the code for testing different scenarios.

## File Descriptions

All code files are located in the `src` folder:

- **`board.py`**: Defines the game board and utility functions for state generation and manipulation.
- **`hill_climbing_and_bfs.py`**: Contains implementations of Hill Climbing and Breadth-First Search algorithms.
- **`informed_search.py`**: Implements A* and Iterative Deepening A* algorithms with heuristics.
- **`rubiks_race_solver_test.py`**: Main script to run and test the solvers.

## Algorithms Overview

- **A***: Uses heuristics to find the optimal solution efficiently.
- **IDA***: A memory-efficient variation of A*.
- **Hill Climbing**: Explores the solution space but may get stuck in local minima.
- **Breadth-First Search**: Guarantees finding a solution but is computationally expensive.

## Results

- **IDA*** with Manhattan Distance heuristic performed best in terms of efficiency and accuracy.
- Hill Climbing was fast but often failed to find a solution due to local minima.

## Future Work

- Investigate genetic algorithms and linear conflict heuristics for improved performance.
- Test scalability with larger grid sizes and more complex patterns.

## References

This project is based on research and techniques used for solving N-Puzzle problems, adapted for Rubik's Race. Detailed insights can be found in the accompanying analysis PDF.

---

For more details, refer to the project report included in `rubiks-race-solver-analysis.pdf`.

