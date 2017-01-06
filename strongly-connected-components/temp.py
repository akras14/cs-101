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

def reverseGraph(graph):
    newGraph = {}
    for k,v in data.items():
        for edge in v:
            if edge not in newGraph:
                newGraph[edge] = [k]
            else:
                newGraph[edge].append(k)
    return newGraph

t = 0 # Number of nodes process so far
s = None # Current source node

def dfsLoop(graph):
    visited = []
    for i in range(len(data), 0, -1):
        if i not in visited:
            leader = i
            dfs(graph, i)

#revData = reverseGraph(data)

def dfs(graph, node):
    visited = []
    next = [node]
    while len(next) > 0:
        node = next.pop()
        if node not in visited:
            visited.append(node)
            next = next + graph[node]
