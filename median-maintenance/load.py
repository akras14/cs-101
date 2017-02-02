"""Load test data"""
import math
import heap

def shouldBalance(left, right):
    """Check if 2 heaps are more than 1 node apart"""
    return math.fabs(left.size() - right.size()) > 1

def balance(left, right):
    """Balance two heaps that are off by 1 value"""
    if left.size() > right.size():
        temp = left.remove()
        right.insert(temp)
    elif left.size() < right.size():
        temp = right.remove()
        left.insert(temp)
    else:
        raise ValueError("Heaps were of same size")

    if shouldBalance(left, right):
        raise ValueError("Balances was called too late")

    return True

FILENAME = "test.txt"
# file = "median.txt"

data = []
with open(FILENAME) as f:
    for num in f:
        data.append(int(num))


median = None
leftHeap = heap.Heap(heap.MAX)
rightHeap = heap.Heap(heap.MIN)

for i, d in enumerate(data):
    if d < median:
        leftHeap.insert(d)
    else:
        rightHeap.insert(d)
    # print "Left"
    # leftHeap.show()
    # print "Right"
    # rightHeap.show()

    if shouldBalance(leftHeap, rightHeap):
        balance(leftHeap, rightHeap)

    if leftHeap.size() > rightHeap.size():
        median = leftHeap.top()
    elif rightHeap.size() > leftHeap.size():
        median = rightHeap.top()
    else:
        median = (leftHeap.top() + rightHeap.top()) / 2.0

    print float(median)
