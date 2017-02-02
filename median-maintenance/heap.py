"""Minimal Heap Implementation"""
import math

MAX = 1
MIN = -1

class Heap(object):

    direction = []
    """Heap"""
    def __init__(self, direction):
        self.items = []
        self.direction = direction

    def __parentId(self, i):
        """Return parent index based on index"""
        return int(math.ceil(i/2.0)) - 1

    def __getFirstChildId(self, i):
        """Return id of left child"""
        return i*2 + 1

    def insert(self, newVal):
        """Add new value to the Heap"""

        self.items.append(newVal)
        childId = len(self.items) - 1

        while childId > 0:
            parentId = self.__parentId(childId)
            parent = self.items[parentId]
            child = self.items[childId]

            if self.direction == MAX:
                shouldSwap = child > parent
            elif self.direction == MIN:
                shouldSwap = child < parent
            else:
                raise ValueError("Unsupported direction")

            if shouldSwap:
                self.items[parentId] = child
                self.items[childId] = parent
                childId = parentId
            else:
                break
    def remove(self):
        """Remove first item, and re-balance the heap"""
        item = None

        if len(self.items) > 0:
            item = self.items[0]
            last = self.items.pop()

            if len(self.items) == 0: #Nothing left to do
                return item
            else:
                self.items[0] = last # Move last node to be the root

            # Bubble down new root to restore Heap property
            parentId = 0
            leftChildId = self.__getFirstChildId(parentId)

            while leftChildId < len(self.items):
                rightChildId = leftChildId + 1
                parent = self.items[parentId]
                left = self.items[leftChildId]

                if rightChildId < len(self.items):
                    right = self.items[rightChildId]
                else:
                    right = None

                if self.direction == MAX:
                    if parent < left or parent < right:
                        if right is None:
                            shouldSwapLeft = True
                        else:
                            shouldSwapLeft = left >= right

                    else: # All done, heap property is restored
                        break
                elif self.direction == MIN:
                    if parent > left or parent > right:
                        if right is None:
                            shouldSwapLeft = True
                        else:
                            shouldSwapLeft = left <= right

                    else: # All done, heap property is restored
                        break
                else:
                    raise ValueError("Unsupported direction")

                if shouldSwapLeft:
                    self.items[leftChildId] = parent
                    self.items[parentId] = left
                    parentId = leftChildId
                    leftChildId = self.__getFirstChildId(parentId)
                else: # Should swap right
                    self.items[rightChildId] = parent
                    self.items[parentId] = right
                    parentId = rightChildId
                    leftChildId = self.__getFirstChildId(parentId)
        return item

    def show(self):
        """Print full heap"""
        print self.items

    def size(self):
        """Get heap size"""
        return len(self.items)
