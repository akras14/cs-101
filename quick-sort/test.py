"""Quick sorts tests"""

from quicksort import sort, partition

def isEqual(arr1, arr2):
    """Check if two arrays are equal"""
    l1 = len(arr1)
    l2 = len(arr2)
    if l1 != l2:
        return False
    for i in range(0, max(len(arr1), len(arr2))):
        if arr1[i] != arr2[i]:
            return False
    return True

def testEquals():
    """Confirm that two arrays are equal"""
    assert isEqual([1, 2, 3], [1, 2, 3])

def testNotEquals():
    """Confirm that two arrays are not equal"""
    assert not isEqual([1, 2, 3], [1, 2, 3, 4])
    assert not isEqual([1, 2, 3, 4], [1, 2, 3])

def testArrayOfOne():
    """Test array of 1 value"""
    arr = [1]
    sort(arr)
    expectedArr = [1]
    assert isEqual(arr, expectedArr)

def testPartition():
    """Test partition function"""
    print "Test"
    arr = [4, 3, 2, 1]
    partition(arr, 0, len(arr) - 1)
    pivoted = [1, 3, 2, 4]
    assert isEqual(arr, pivoted)


def testArrayOfTwoSorted():
    """Test array of 2 value already sorted"""
    arr = [1, 2]
    sort(arr)
    expectedArr = [1, 2]
    assert isEqual(arr, expectedArr)

def testArrayOfTwoNotSorted():
    """Test array of 2 value not yet sorted"""
    arr = [2, 1]
    sort(arr)
    expectedArr = [1, 2]
    assert isEqual(arr, expectedArr)

def testLargeArrayReverse():
    """Test quick sort revered"""
    arr = [5, 4, 3, 2, 1]
    sort(arr)
    expectedArr = [1, 2, 3, 4, 5]
    assert isEqual(arr, expectedArr)

def testLargeArrayMixed():
    """Test quick sort random"""
    arr = [1, 4, 3, 5, 2]
    sort(arr)
    expectedArr = [1, 2, 3, 4, 5]
    assert isEqual(arr, expectedArr)

def testLargerArray():
    """Test array of 10 items"""
    arr = [7, 4, 9, 6, 3, 8, 1, 5, 2]
    sort(arr)
    expectedArr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert isEqual(arr, expectedArr)


def testRandomLargeArray():
    """Test quick sort random"""
    arr = range(1, 100)
    import random
    random.shuffle(arr)
    print arr
    sort(arr)
    print arr
    expectedArr = range(1, 100)
    assert isEqual(arr, expectedArr)
