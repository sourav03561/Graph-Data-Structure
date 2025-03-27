def adjacency_matrix_to_list(matrix):
    adj_list = {}
    for i in range(len(matrix)):
        adj_list[i] = [j for j in range(len(matrix[i])) if matrix[i][j] == 1]
    return adj_list

adj_matrix = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

adj_list = adjacency_matrix_to_list(adj_matrix)
print(adj_list)