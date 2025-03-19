from collections import deque

def bfs(graph,start, search_value):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()

        if vertex == search_value:
            return True
        
        visited.add(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return False