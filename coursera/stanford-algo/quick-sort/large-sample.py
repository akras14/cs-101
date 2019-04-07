""" Test quick sort on a large data set """

from quicksort import sort
from test import isEqual

data = [int(line.rstrip()) for line in open("./quick-sort-data.txt")]

count = {
    "total": 0
}

sort(data, count=count)

assert isEqual(data, range(1,10001))

print "All done"
print count["total"]