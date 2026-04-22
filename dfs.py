graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(node, visited=[]):
    if node not in visited:
        visited.append(node)
        print(node, end=' ')
        for neighbor in graph[node]:
            dfs(neighbor, visited)

dfs('A')