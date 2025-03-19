def topological_sort_dfs(graph):
    visited = []
    stack = []

    def dfs(node):
        if node not in visited:
            visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)
        stack.apppend(node)
    
    for node in graph:
        if node not in visited:
            dfs(node)
    return stack[::-1]