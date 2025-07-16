import heapq
import itertools
from core.state import State
from core.heuristics import misplaced_tiles, manhattan_distance

def a_star(start: State, heuristic: str = "manhattan") -> State:
    if start.is_goal():
        start.expanded_nodes = 0
        return start

    visited = set()
    heap = []
    counter = itertools.count()
    h_func = manhattan_distance if heuristic == "manhattan" else misplaced_tiles
    heapq.heappush(heap, (h_func(start), 0, next(counter), start))
    expanded = 0

    while heap:
        f, g, _, current = heapq.heappop(heap)
        if current in visited:
            continue
        visited.add(current)
        expanded += 1

        if current.is_goal():
            current.expanded_nodes = expanded
            return current

        for neighbor in current.get_neighbors():
            if neighbor not in visited:
                h = h_func(neighbor)
                heapq.heappush(heap, (g + 1 + h, g + 1, next(counter), neighbor))
    return None