def dfs(graph, start, search_value, visited=None):
    if visited is None:
        visited = set()
    
    if start == search_value:
        return True
    
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            found = dfs(graph, neighbor, search_value, visited)
            if found:
                return True
    return False