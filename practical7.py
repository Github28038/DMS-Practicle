def is_complete_graph(adj_list):
    num_vertices = len(adj_list)

    # A complete graph should have all vertices connected to each other
    for i in range(num_vertices):
        if len(adj_list[i]) != num_vertices - 1:
            return False

    return True

# Example usage
adjacency_list = [
    [1, 2, 3],
    [0, 2, 3],
    [0, 1, 3],
    [0, 1, 2]
]

if is_complete_graph(adjacency_list):
    print("The graph is a complete graph.")
else:
    print("The graph is not a complete graph.")
