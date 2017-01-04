data = []
with open("data.txt") as f:
  for line in f:
    u, v = line.split()
    u = int(u)
    v = int(v)
    data.append((u,v))

print len(data)
