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

    def show(self):
        """Print full heap"""
        print self.items

    def size(self):
        """Get heap size"""
        return len(self.items)
