from inversions import count_inversions as ci

data = [int(line.rstrip()) for line in open("./integers.txt")]
result = ci(data)
print result[0]
print result[1]
