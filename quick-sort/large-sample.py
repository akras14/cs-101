""" Test quick sort on a large data set """

from quicksort import sort
from test import isEqual

data = [int(line.rstrip()) for line in open("./quick-sort-data.txt")]

sort(data)
assert isEqual(data, range(1,10001))

print "All done"