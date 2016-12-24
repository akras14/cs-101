""" Quick Sort Implementation"""

def sort(arr, l=None, r=None):
    """Sort Array"""

    # Init l and r, if not provided
    if l is None:
        l = 0
    if r is None:
        r = len(arr) - 1

    # Check for Base case
    if l >= r: # Length equal 1
        return

    p = getP(arr, l, r)

    p = partition(arr, p, r)
    print "partition is done"
    print arr

    print "First recursion"
    print "l is " + str(l)
    print "p is " + str(p)

    sort(arr, l, p)
    print "Second recursion"
    print "p + 1 is " + str(p + 1)
    print "r is " + str(r)
    sort(arr, p + 1, r)

def partition(arr, l, r):
    """
    Partition array around split point p
    All values to the left of p are less than value at p
    All values to the right of p are greater than value at p

    arr - Array to partition
    l - starting element
    r - right most element
    """
    p = arr[l]

    i = l + 1
    for j in range(l+1, r+1):
        if arr[j] < p:
            swap(arr, i, j)
            i = i + 1
    swap(arr, l, i-1)
    return i - 1

def swap(arr, i, j):
    """Swap two values in an array"""
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = temp

def getP(arr, l, r):
    return l # First element
    # return r # Last element
