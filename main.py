import random
import copy
from core.board import Board
from core.state import State
from core.display import print_grid
from search.a_star import a_star
from search.ida_star import IDAStar
from search.hill_climbing import HillClimbing
from search.bfs import bfs

def generate_random_grid(n):
    colors = ['R', 'G', 'B', 'Y', 'O', 'P']
    count = (n * n - 1) // len(colors)
    tiles = sum([[c] * count for c in colors], [])
    random.shuffle(tiles)
    while True:
        insert_pos = random.randint(0, len(tiles))
        trial = tiles[:]
        trial.insert(insert_pos, '_')
        grid = [trial[i*n:(i+1)*n] for i in range(n)]
        if '_' not in [grid[i][j] for i in range(1, n-1) for j in range(1, n-1)]:
            return grid

def move_away(grid, steps):
    board = Board(grid)
    for _ in range(steps):
        moves = board.get_possible_moves()
        move = random.choice(moves)
        board = board.move(move)
    return board.grid

def print_solver_result(name, result):
    print(f"Solving using {name}...")
    if result is None:
        print(f"No solution found by {name}")
    else:
        expanded = getattr(result, "expanded_nodes", None)
        if expanded is not None:
            print(f"Nodes expanded ({name}):\t\t{expanded}")
        else:
            print(f"Solution found by {name} (no node count tracked)")

def main():
    n = 5
    goal_grid = generate_random_grid(n)
    initial_grid = move_away(copy.deepcopy(goal_grid), 10)
    initial_board = Board(initial_grid)
    goal_board = Board(goal_grid)
    state = State(initial_board, goal_board)

    print("Initial Board:")
    print_grid(initial_board.grid)

    print("Goal Window:")
    print_grid(goal_board.extract_goal_window())

    print_solver_result("A*", a_star(state))
    print_solver_result("IDA*", IDAStar().search(state))
    print_solver_result("Hill Climbing", HillClimbing().search(state))
    print_solver_result("BFS", bfs(state))

if __name__ == "__main__":
    main()
