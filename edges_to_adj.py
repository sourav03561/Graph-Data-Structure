from collections import defaultdict
edges = [[0,1],[1,2],[2,0]]
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

print(graph)
