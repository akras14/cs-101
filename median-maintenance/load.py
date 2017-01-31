"""Load test data"""

data = []
with open("median.txt") as f:
    for num in f:
        data.append(int(num))


for i, d in enumerate(data):
    print d
