""" Quick Sort Implementation"""

def sort(arr, l=None, r=None, count=None):
    """Sort Array"""

    # Init l and r, if not provided
    if l is None:
        l = 0
    if r is None:
        r = len(arr) - 1

    # Check for Base case
    if l >= r: # Length equal 1
        return

    if count is not None:
        count["total"] += r - l

    p = getP(arr, l, r)
    swap(arr, p, l)

    p = partition(arr, l, r)

    sort(arr, l, p - 1, count)
    sort(arr, p + 1, r, count)

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
    # return l # First element
    # return r # Last element
    return medianPivotPoint(arr, l, r)

def medianPivotPoint(arr, l, r):
    arrLength = r - l + 1
    if arrLength < 3:
        return l
    left = arr[l]
    right = arr[r]

    if arrLength % 2 == 0: # Even
        middleIndex = l + arrLength / 2 - 1
    else: # Odd
        middleIndex = l + arrLength / 2

    middle = arr[middleIndex]

    maxVal = max(left, middle, right)
    minVal = min(left, middle, right)

    if left != maxVal and left != minVal:
        return l
    elif right != maxVal and right != minVal:
        return r
    elif middle != maxVal and middle != maxVal:
        return middleIndex
    else:
        raise ValueError
