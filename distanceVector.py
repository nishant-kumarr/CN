def distance_vector_routing(graph):
    # Number of vertices in the graph
    n = len(graph)

    # Initialize distance vectors for each node
    distance_vectors = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        distance_vectors[i][i] = 0  # Distance to itself is 0

    # Initially set distances from the adjacency matrix
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:  # There's a direct edge
                distance_vectors[i][j] = graph[i][j]

    # Distance Vector Algorithm
    updated = True
    while updated:
        updated = False
        for i in range(n):  # For each node
            for j in range(n):  # For each destination
                for k in range(n):  # For each neighbor
                    if distance_vectors[i][j] > distance_vectors[i][k] + distance_vectors[k][j]:
                        distance_vectors[i][j] = distance_vectors[i][k] + distance_vectors[k][j]
                        updated = True  # A change was made, so we continue updating

    return distance_vectors

# Example graph as an adjacency matrix
graph = [
    [0, 2, 0, 1, 0],
    [2, 0, 3, 2, 0],
    [0, 3, 0, 0, 1],
    [1, 2, 0, 0, 4],
    [0, 0, 1, 4, 0]
]

result = distance_vector_routing(graph)

print("Distance Vector Table:")
for i in range(len(result)):
    print(f"From node {i}: {result[i]}")
