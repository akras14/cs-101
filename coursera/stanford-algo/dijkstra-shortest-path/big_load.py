"""Load test data and run DI on it"""

from graph import Graph
from di import di

test = Graph()
with open("dijkstraData.txt") as f:
    for d in f:
        d = d.strip().split('\t')
        from_node = int(d[0])
        for e in d[1:]:
            e = e.split(',')
            to_node = int(e[0])
            distance = int(e[1])
            test.add_edge(from_node, to_node, distance)

data = di(test, 1)
test = "7,37,59,82,99,115,133,165,188,197".split(",")
test = map(int, test)
res = []
for t in test:
    res.append(str(data[t]))

print ",".join(res)