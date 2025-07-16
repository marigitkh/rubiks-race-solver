from typing import List, Optional
from core.board import Board

class State:
    def __init__(self, board: Board, goal: Board, path: Optional[List[str]] = None):
        self.board = board
        self.goal = goal
        self.path = path if path is not None else []

    def is_goal(self) -> bool:
        board_window = self.board.extract_goal_window()
        goal_window = self.goal.extract_goal_window()
        return board_window == goal_window

    def get_neighbors(self) -> List['State']:
        neighbors = []
        for move in self.board.get_possible_moves():
            new_board = self.board.move(move)
            if new_board != self.board:
                neighbors.append(State(new_board, self.goal, self.path + [move]))
        return neighbors

    def __hash__(self):
        return hash(self.board)

    def __eq__(self, other: 'State') -> bool:
        return self.board == other.board