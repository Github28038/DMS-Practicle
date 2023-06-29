def compute_degree(graph):
    num_vertices = len(graph)
    in_degrees = [0] * num_vertices
    out_degrees = [0] * num_vertices

    for row in graph:
        for col in row:
            out_degrees[col] += 1
            in_degrees[row[0]] += 1

    return in_degrees, out_degrees

# Example usage
graph = [
    [0, 1],  # Edge 0 -> 1
    [1, 2],  # Edge 1 -> 2
    [2, 0]   # Edge 2 -> 0
]

in_degrees, out_degrees = compute_degree(graph)

print("Vertex\tIn-degree\tOut-degree")
for i in range(len(in_degrees)):
    print(i, "\t", in_degrees[i], "\t\t", out_degrees[i])
