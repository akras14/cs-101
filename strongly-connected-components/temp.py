data = {
    1: [4],
    2: [8],
    3: [6],
    4: [7],
    5: [2],
    6: [9],
    7: [1],
    8: [5, 6],
    9: [3, 7]
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
finish_time = {}
leaders = {}
visited = []
def dfsLoop(graph):
    global s
    for i in range(len(data), 0, -1): # All nodes in reverse order
        if i not in visited:
            s = i
            dfs(graph, i)

def dfs(graph, node):
    global t
    if node not in visited:
        visited.append(node)
        leaders[node] = s
    for next in graph[node]:
        if next not in visited:
            dfs(graph, next)
    t += 1
    finish_time[node] = t

revData = reverseGraph(data)
dfsLoop(revData)
print finish_time