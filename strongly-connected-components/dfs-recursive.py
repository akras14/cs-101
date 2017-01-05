data = {
    1: [7],
    2: [5],
    3: [9],
    4: [1],
    5: [8],
    6: [3, 8],
    7: [4, 9],
    8: [2],
    9: [6],
}

visited = []
def dfs(graph, node):
    if node not in visited:
        print node
        visited.append(node)
    for next in graph[node]:
        if next not in visited:
            dfs(graph, next)

dfs(data, 7)