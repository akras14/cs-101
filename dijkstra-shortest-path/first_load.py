from graph import Graph
test = Graph()
with open("test-1.txt") as f:
    for d in f:
        d = d.strip().split('\t')
        from_node = int(d[0])
        for e in d[1:]:
            e = e.split(',')
            to_node = int(e[0])
            distance = int(e[1])
            test.add_edge(from_node, to_node, distance)
test.show()
