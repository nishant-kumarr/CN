import sys

def dijkstra(graph, start):
    # Number of vertices in the graph
    n = len(graph)

    # Distance from start to each vertex
    distances = [sys.maxsize] * n
    distances[start] = 0  # Distance to the start vertex is 0

    # Visited set to keep track of processed nodes
    visited = [False] * n

    for _ in range(n):
        # Find the unvisited vertex with the smallest distance
        min_distance = sys.maxsize
        min_index = -1
        for v in range(n):
            if not visited[v] and distances[v] < min_distance:
                min_distance = distances[v]
                min_index = v

        # Mark the chosen vertex as visited
        visited[min_index] = True

        # Update the distances of the neighbors of the chosen vertex
        for neighbor in range(n):
            if graph[min_index][neighbor] > 0 and not visited[neighbor]:
                new_distance = distances[min_index] + graph[min_index][neighbor]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

    return distances

# Example graph as an adjacency matrix
graph = [
    [0, 10, 0, 0, 0, 0],
    [10, 0, 5, 0, 0, 0],
    [0, 5, 0, 20, 1, 0],
    [0, 0, 20, 0, 2, 5],
    [0, 0, 1, 2, 0, 3],
    [0, 0, 0, 5, 3, 0]
]

start_vertex = 0
print(f"Shortest distances from vertex {start_vertex}: {dijkstra(graph, start_vertex)}")
