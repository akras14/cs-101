startData = [
    [1,2,3],
    [2,1,3,4],
    [3,1,2,4],
    [4,3,2]
]

import random
import time
from copy import deepcopy

def getRandomRowAndColumn(data):
    rowIndex = random.randint(0, len(data) - 1)
    row = data[rowIndex]
    columnIndex = random.randint(1, len(row) - 1) # Ignore first value - Node label
    return (rowIndex, columnIndex)

def findNodeToMerge(label, data):
    index = -1
    for i,d in enumerate(data):
        if d[0] == label:
            index = i
    return index

def findCuts(data):
    while len(data) > 2:
        # print "Still working " + str(len(data))
        rowIndex, columnIndex = getRandomRowAndColumn(data)
        edge = data[rowIndex][columnIndex]

        nodeToKeep = data[rowIndex]
        nodeToMergeIndex = findNodeToMerge(edge, data)
        nodeToMerge = data.pop(nodeToMergeIndex) # Removes node from data
        
        keepLabel = nodeToKeep[0]
        mergeLabel = nodeToMerge[0]

        # Store all merge items
        for e in nodeToMerge:
            nodeToKeep.append(e)

        # Replace all other references to old label with new label
        for r in data:
            for i,c in enumerate(r):
                if c == mergeLabel:
                    r[i] = keepLabel

        # Remove self loops
        for di,r in enumerate(data):
            for i,c in enumerate(r):
                if i > 0 and c == r[0]:
                    r[i] = -1
            data[di] = filter(lambda x: x != -1, r)
    return len(data[0]) - 1

def findMin(data):
    minVal = findCuts(deepcopy(data))
    for i in range(1, 100):
        print i
        temp = findCuts(deepcopy(data))
        if temp < minVal:
            minVal = temp
    print "Min Val is"
    return minVal

