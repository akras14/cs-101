import heap

test = heap.Heap(heap.MIN)
# test = heap.Heap(heap.MAX)


test.insert(3)
test.insert(3)
test.insert(3)
test.insert(3)
test.insert(2)
test.insert(2)
test.insert(1)

test.show()

print test.size()

print "Removing"

print test.remove()
test.show()
print test.remove()
test.show()
print test.remove()
test.show()
print test.remove()
test.show()
print test.remove()
test.show()
print test.remove()
test.show()
print test.remove()
test.show()
print test.remove()
test.show()
print test.remove()
test.show()
