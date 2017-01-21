data = { # 6,3,2,1,0
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

# data = {  # 3,3,2,0,0
#     1: [ 2],
#     2: [ 6,3,4],
#     3: [ 1,4],
#     4: [ 5],
#     5: [ 4],
#     6: [ 5,7],
#     7: [ 6,8],
#     8: [ 5,7]
# }

# data = { # 7,1,0,0,0
#     1: [2],
#     2: [3],
#     3: [1,4],
#     4: [3, 6],
#     5: [4],
#     6: [4,7],
#     8: [6],
#     7: [8]
# }

data = { # 6,3,2,1,0
    1: [2],
    2: [3,4,5],
    3: [6],
    4: [5,7],
    5: [2,6,7],
    6: [3,8],
    7: [8,10],
    8: [7],
    9: [7],
    10: [9,11],
    11: [12],
    12: [10]
}

# data = {}
# with open("data.txt") as f:
#   for line in f:
#     u, v = line.split()
#     u = int(u)
#     v = int(v)
#     if u in data:
#         data[u].append(v)
#     else:
#         data[u] = [v]

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
            # print "Checking for " + str(i)
            s = i
            dfs(graph, i)

def allFinished(graph):
    allNextVisited = True
    for n in graph:
        if n not in visited:
            allNextVisited = False   
    return allNextVisited 
def dfs(graph, node):
    global t
    finish_time_stack = []

    if node not in visited:
        leaders[node] = s
    if node in graph:
        stack = [node]
        while len(stack) > 0:
            next = stack.pop(0)
            if next not in visited:           
                print next
                visited.append(next)
                if next in graph:
                    stack = graph[next] + stack
                
                if next not in graph or allFinished(graph[next]):
                    t += 1
                    finish_time[next] = t
                    if len(finish_time_stack) > 0:                
                        last = finish_time_stack.pop()
                    else:
                        last = None
                    print "last is " + str(last)
                    while last and allFinished(graph[last]):
                        t += 1
                        finish_time[last] = t
                        if len(finish_time_stack) > 0:
                            last = finish_time_stack.pop()
                        else:
                            last = None
                    if last:
                        finish_time_stack.append(last)
                else:
                    finish_time_stack.append(next)
            print finish_time_stack


revData = reverseGraph(data)
print revData
dfsLoop(revData)
print finish_time
finishTimeData = finTimeData(data, finish_time)

# Second Pass
visited = []
dfsLoop(finishTimeData)

lead = sorted(set(leaders.values()), reverse=True)
visited = []
scc = [0]*5
for l in lead:
    t = 0
    dfs(finishTimeData, l)
    scc.append(t)

print sorted(scc, reverse=True)[:5]

