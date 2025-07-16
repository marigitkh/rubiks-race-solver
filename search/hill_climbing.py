import random
from core.state import State
from core.heuristics import manhattan_distance, misplaced_tiles

class HillClimbing:
    def __init__(self, heuristic: str = "manhattan"):
        self.h_func = manhattan_distance if heuristic == "manhattan" else misplaced_tiles

    def search(self, state: State) -> State:
        if state.is_goal():
            state.expanded_nodes = 0
            return state

        current = state
        expanded = 0
        while True:
            neighbors = current.get_neighbors()
            if not neighbors:
                break
            expanded += len(neighbors)
            scored = [(self.h_func(n), n) for n in neighbors]
            scored.sort(key=lambda x: x[0])
            best_score, best = scored[0]
            if self.h_func(current) <= best_score:
                break  # No improvement
            current = best
            if current.is_goal():
                current.expanded_nodes = expanded
                return current
        return current if current.is_goal() else None