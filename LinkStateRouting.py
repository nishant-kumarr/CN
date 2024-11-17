import sys

def path_finder(graph, start):
    n = len(graph)
    visited = [False] * n
    distances = [sys.maxsize] * n
    distances[start] = 0
    previous = [-1] * n  # To reconstruct the path if needed

    for _ in range(n):
        # Select the unvisited node with the smallest distance
        min_distance = sys.maxsize
        min_index = -1
        for i in range(n):
            if not visited[i] and distances[i] < min_distance:
                min_distance = distances[i]
                min_index = i

        visited[min_index] = True

        # Update the distances of neighbors
        for neighbor in range(n):
            if graph[min_index][neighbor] > 0 and not visited[neighbor]:
                new_distance = distances[min_index] + graph[min_index][neighbor]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = min_index

    return distances

def link_state_routing(graph):
    n = len(graph)
    for start in range(n):
        print(f"\nRouter {start}: Computing shortest paths to all other routers...")
        distances = path_finder(graph, start)
        print(f"Shortest distances from Router {start}: {distances}")

# Example graph as an adjacency matrix (0 means no direct link)
graph = [
    [0, 2, 0, 1, 0],
    [2, 0, 3, 2, 0],
    [0, 3, 0, 0, 1],
    [1, 2, 0, 0, 3],
    [0, 0, 1, 3, 0]
]

# Run the Link State Routing algorithm
link_state_routing(graph)
