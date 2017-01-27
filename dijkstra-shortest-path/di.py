"""Dijkstra's Algorithm"""
# pylint: disable=C0103

def di(graph, node):
    """Compute Dijkstra shortest path"""
    visited = {}
    dist = {}
    all_nodes = graph.get_nodes()
    for n in all_nodes:
        dist[n] = 10000
        visited[n] = False
    v = node
    dist[v] = 0

    while visited[v] == False:
        visited[v] = True
        edges = graph.get_edges(v)

        while len(edges) > 0:
            w, weight = edges.pop(0)
            if dist[w] > (dist[v]+weight):
                dist[w] = dist[v] + weight
        v = 1
        minDist = 10000
        for i in range(1, graph.size() + 1):
            if visited[i] == False and minDist > dist[i]:
                minDist = dist[i]
                v = i
    return dist

