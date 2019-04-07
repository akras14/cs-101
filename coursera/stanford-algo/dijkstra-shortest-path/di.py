"""Dijkstra's Algorithm"""
# pylint: disable=C0103

def di(graph, node):
    """Compute Dijkstra shortest path"""
    MAX_DIST = 10000
    visited = {}
    dist = {}
    all_nodes = graph.get_nodes()
    for n in all_nodes:
        dist[n] = MAX_DIST
        visited[n] = False
    v = node
    dist[v] = 0

    while visited[v] is False:
        visited[v] = True
        edges = graph.get_edges(v)

        while len(edges) > 0:
            w, weight = edges.pop(0)
            if dist[w] > (dist[v]+weight):
                dist[w] = dist[v] + weight
        v = 1
        minDist = MAX_DIST
        for i in range(1, graph.size() + 1):
            if visited[i] is False and minDist > dist[i]:
                minDist = dist[i]
                v = i
    return dist

