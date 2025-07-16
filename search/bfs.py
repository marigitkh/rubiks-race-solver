from collections import deque
from core.state import State

def bfs(start: State) -> State:
    if start.is_goal():
        start.expanded_nodes = 0
        return start

    queue = deque([start])
    visited = set()
    expanded = 0

    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        expanded += 1

        if current.is_goal():
            current.expanded_nodes = expanded
            return current

        for neighbor in current.get_neighbors():
            if neighbor not in visited:
                queue.append(neighbor)
    return None