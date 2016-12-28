import csv
with open("data.txt") as f:
    data = {}
    for line in csv.reader(f, dialect="excel-tab"):
        data[int(line[0])] = map(lambda x: int(x), line[1:-1])

print data
