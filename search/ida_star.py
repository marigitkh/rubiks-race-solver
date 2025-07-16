from core.heuristics import misplaced_tiles, manhattan_distance
from core.state import State

class IDAStar:
    def __init__(self, heuristic: str = "manhattan"):
        self.h_func = manhattan_distance if heuristic == "manhattan" else misplaced_tiles
        self.nodes_expanded = 0

    def search(self, state: State) -> State:
        if state.is_goal():
            state.expanded_nodes = 0
            return state
        threshold = self.h_func(state)
        while True:
            self.nodes_expanded = 0
            temp = self._dfs(state, 0, threshold, set())
            if isinstance(temp, State):
                temp.expanded_nodes = self.nodes_expanded
                return temp
            if temp == float("inf"):
                return None
            threshold = temp

    def _dfs(self, state: State, g: int, threshold: int, visited: set):
        self.nodes_expanded += 1
        f = g + self.h_func(state)
        if f > threshold:
            return f
        if state.is_goal():
            return state

        min_threshold = float("inf")
        visited.add(state)
        for neighbor in state.get_neighbors():
            if neighbor in visited:
                continue
            result = self._dfs(neighbor, g + 1, threshold, visited)
            if isinstance(result, State):
                return result
            min_threshold = min(min_threshold, result)
        visited.remove(state)
        return min_threshold