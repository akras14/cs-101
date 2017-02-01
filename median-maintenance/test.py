import heap

print heap.MIN

test = heap.Heap(heap.MAX)


test.insert(3)
test.insert(3)
test.insert(3)
test.insert(3)
test.insert(2)
test.insert(2)
test.insert(1)

test.show()

print test.size()