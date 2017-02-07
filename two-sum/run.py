"""Find two sums count for distinct pair in specified file"""

source = 'data.txt'
test = range(-10000, 10001)

#source = 'test.txt'
#test = [3,10]

with open(source) as f:
    data = map(int, f.readlines())

vals = set()
for d in data:
    vals.add(d)

def findSum(target):
    """Find all two sums for target"""
    seen = {}
    for val in data:
        needed = target - val
        if needed in vals:
            pair = (val, needed)
            if pair not in seen:
                seen[pair] = True
                return True
    return False


total = 0
for t in test:
    if findSum(t) == True:
        total += 1
    if t % 100 == 0:
        print t
        print total
print "Done"
print total
