data = {}
with open("data.txt") as f:
  for line in f:
    u, v = line.split()
    u = int(u)
    v = int(v)
    if u in data:
        data[u].append(v)
    else:
        data[u] = [v]

print len(data)
