def adjacency_matrix_to_list(matrix):
    adj_list = {}
    for i in range(len(matrix)):
        # Only include connections to other nodes, ignoring self-loops
        adj_list[i + 1] = [j + 1 for j in range(len(matrix[i])) if matrix[i][j] == 1 and i != j]
    return adj_list

isConnected = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

adj_list = adjacency_matrix_to_list(isConnected)
print(adj_list)
