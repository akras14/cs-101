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


t = 0 # Number of nodes process so far
s = None # Current source node

finish_time = {}
leaders = {}
visited = []

def reverseGraph(graph):
    newGraph = {}
    for k,v in data.items():
        for edge in v:
            if edge not in newGraph:
                newGraph[edge] = [k]
            else:
                newGraph[edge].append(k)
    return newGraph


def finTimeData(data, finish_time):
    newGraph = {}
    for k,v in data.items():
        newK = finish_time[k]
        newEdges = []
        for edge in v:
            newEdge = finish_time[edge]
            newEdges.append(newEdge)
        newGraph[newK] = newEdges
    return newGraph

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
    if node in graph:
        for next in graph[node]:
            if next not in visited:
                dfs(graph, next)
    t += 1
    finish_time[node] = t

revData = reverseGraph(data)
dfsLoop(revData)

finishTimeData = finTimeData(data, finish_time)

# Second Pass
visited = []
dfsLoop(finishTimeData)

lead = sorted(set(leaders.values()), reverse=True)
print lead
visited = []
for l in lead:
    t = 0
    dfs(finishTimeData, l)
    print l
    print t
    print "--"

