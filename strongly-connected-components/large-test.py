# Total Node count is 875714
# Some nodes don't have edges
# Via the following code
# nodes = []
# with open("data.txt") as f:
#     for line in f:
#         u, v = line.split()
#         u = int(u)
#         v = int(v)
#         nodes.append(u)
#         nodes.append(v)
# len(set(first))
# len(set(nodes))

TOTAL_NODE_COUNT = 875714
data = {}
for i in range(0, TOTAL_NODE_COUNT):
    data[i] = []
with open("data.txt") as f:
  for line in f:
    u, v = line.split()
    u = int(u)
    v = int(v)
    data[u].append(v)

print len(data)