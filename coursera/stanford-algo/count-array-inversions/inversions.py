def count_inversions(arr):
    invCount = 0
    if len(arr) < 2:
        return (arr, invCount) 
    middle = len(arr) / 2
    leftArr, leftCount = count_inversions(arr[:middle])
    rightArr, rightCount = count_inversions(arr[middle:])
    
    mergedArr, mergeCount = merge_and_count(leftArr, rightArr)

    invCount += leftCount + rightCount + mergeCount
    return (mergedArr, invCount)

def merge_and_count(leftArr, rightArr):
    invCount = 0
    mergedArr = []
    while len(leftArr) > 0 or len(rightArr) > 0:
        if len(leftArr) == 0:
            mergedArr.append(rightArr.pop(0))
        elif len(rightArr) == 0:
            mergedArr.append(leftArr.pop(0))
        elif leftArr[0] > rightArr[0]:
            invCount += len(leftArr)
            mergedArr.append(rightArr.pop(0))
        elif rightArr[0] > leftArr[0]:
            mergedArr.append(leftArr.pop(0))
        else:
            raise ValueError("All inputs are expected to be unique")
    return (mergedArr, invCount)
