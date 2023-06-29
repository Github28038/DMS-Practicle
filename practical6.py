def is_complete_graph(adj_matrix):
    num_vertices = len(adj_matrix)

    # A complete graph should have all entries except the diagonal as 1
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i != j and adj_matrix[i][j] != 1:
                return False

    return True

# Example usage
adjacency_matrix = [
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0]
]

if is_complete_graph(adjacency_matrix):
    print("The graph is a complete graph.")
else:
    print("The graph is not a complete graph.")
