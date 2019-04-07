import csv
from mincut import findMin
with open("data.txt") as f:
    data = []
    for line in csv.reader(f, dialect="excel-tab"):
        data.append(line[:-1])
print findMin(data)
