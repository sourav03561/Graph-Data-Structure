class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(graph,src,vis):
            stack = []
            stack.append(src)
            while stack:
                node = stack.pop(-1)
                if node not in vis:
                    vis.add(node)
                    for neighbour in graph[node]:
                        if neighbour not in vis:
                            stack.append(neighbour)

        adj_list = {}
        for i in range(len(isConnected)):
        # Only include connections to other nodes, ignoring self-loops
            adj_list[i + 1] = [j + 1 for j in range(len(isConnected[i])) if isConnected[i][j] == 1 and i != j]
        
        no_of_province = 0
        vis = set()
        for i in adj_list:
            if i not in vis:
                no_of_province+=1
                dfs(adj_list,i,vis)
        return no_of_province
