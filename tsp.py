from itertools import permutations

def tsp(graph, start):
    cities = list(graph.keys())
    cities.remove(start)

    min_cost = float('inf')
    best_path = []

    for perm in permutations(cities):
        path = [start] + list(perm) + [start]
        cost = 0
        valid = True

        for i in range(len(path) - 1):
            if path[i+1] in graph[path[i]]:
                cost += graph[path[i]][path[i+1]]
            else:
                valid = False
                break

        if valid and cost < min_cost:
            min_cost = cost
            best_path = path

    print(f"\nTSP Best Path: {best_path}")
    print(f"Minimum Cost: {min_cost}")

# Example
tsp_graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}
tsp(tsp_graph, 'A')


