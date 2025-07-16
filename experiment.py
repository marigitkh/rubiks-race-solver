import random
import copy
import pandas as pd
from core.board import Board
from core.state import State
from search.a_star import a_star
from search.ida_star import IDAStar
from search.hill_climbing import HillClimbing
from search.bfs import bfs
from main import generate_random_grid, move_away

def run_solver(solver_name, state):
    if solver_name == "A*":
        result = a_star(state)
    elif solver_name == "IDA*":
        result = IDAStar().search(state)
    elif solver_name == "Hill Climbing":
        result = HillClimbing().search(state)
    elif solver_name == "BFS":
        result = bfs(state)
    else:
        raise ValueError("Unknown solver")

    if result is None:
        return False, None
    return result.is_goal(), getattr(result, "expanded_nodes", None)

def run_experiments(distances=[10, 20, 30, 40, 50], seeds_per_distance=10, board_size=5):
    results = []

    for dist in distances:
        for seed in range(seeds_per_distance):
            random.seed(seed)
            goal_grid = generate_random_grid(board_size)
            initial_grid = move_away(copy.deepcopy(goal_grid), dist)

            goal_board = Board(goal_grid)
            initial_board = Board(initial_grid)
            state = State(initial_board, goal_board)

            for solver_name in ["A*", "IDA*", "Hill Climbing", "BFS"]:
                solved, nodes = run_solver(solver_name, state)
                results.append({
                    "Distance": dist,
                    "Seed": seed,
                    "Solver": solver_name,
                    "Solved": solved,
                    "NodesExpanded": nodes if nodes is not None else "N/A"
                })

    return pd.DataFrame(results)

if __name__ == "__main__":
    df = run_experiments()
    print(df)
    df.to_csv("experiment_results.csv", index=False)