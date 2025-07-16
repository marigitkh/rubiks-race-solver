from typing import List, Tuple
import copy

Grid = List[List[str]]
Position = Tuple[int, int]

class Board:
    def __init__(self, grid: Grid):
        self.grid = grid
        self.n = len(grid)
        self.empty = self.find_empty()

    def find_empty(self) -> Position:
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] == "_":
                    return (i, j)
        raise ValueError("No empty space found in the board")

    def display(self):
        for row in self.grid:
            print(" ".join(row))
        print()

    def copy(self) -> 'Board':
        return Board(copy.deepcopy(self.grid))

    def move(self, direction: str) -> 'Board':
        di = {'up': -1, 'down': 1, 'left': 0, 'right': 0}
        dj = {'up': 0, 'down': 0, 'left': -1, 'right': 1}
        i, j = self.empty
        ni, nj = i + di[direction], j + dj[direction]
        if 0 <= ni < self.n and 0 <= nj < self.n:
            new_grid = copy.deepcopy(self.grid)
            new_grid[i][j], new_grid[ni][nj] = new_grid[ni][nj], new_grid[i][j]
            return Board(new_grid)
        return self

    def get_possible_moves(self) -> List[str]:
        i, j = self.empty
        moves = []
        if i > 0: moves.append("up")
        if i < self.n - 1: moves.append("down")
        if j > 0: moves.append("left")
        if j < self.n - 1: moves.append("right")
        return moves

    def extract_goal_window(self) -> Grid:
        return [row[1:-1] for row in self.grid[1:-1]]

    def flatten(self) -> Tuple:
        return tuple(tile for row in self.grid for tile in row)

    def __eq__(self, other: 'Board') -> bool:
        return self.grid == other.grid

    def __hash__(self):
        return hash(self.flatten())