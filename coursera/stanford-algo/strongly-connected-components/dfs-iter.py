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


def dfs(graph, node):
    visited = []
    next = [node]
    while len(next) > 0:
        node = next.pop()
        if node not in visited:
            print node
            visited.append(node)
            next = next + graph[node]

dfs(data, 1)