from inversions import count_inversions as ci

testCases = [
#    {
#        'input': [],
#        'output': [],
#        'result': 0
#    },
#    {
#        'input': [1],
#        'output': [1],
#        'result': 0
#    },
#    {
#        'input': [1, 2],
#        'output': [1, 2],
#        'result': 0
#    },
#    {
#        'input': [2, 1],
#        'output': [1, 2],
#        'result': 1
#    },
    {
        'input': [3, 2, 1],
        'output': [1, 2, 3],
        'result': 3
    },
    {
        'input': [1, 2, 3],
        'output': [1, 2, 3],
        'result': 0
    },
    {
        'input': [2, 1, 3],
        'output': [1, 2, 3],
        'result': 1
    },
    {
        'input': [6,5,4,3,2,1],
        'output': [1,2,3,4,5,6],
        'result': 15
    },
]

def test_inv_count():
    for t in testCases:
        sortedArray, invCount = ci(t['input'])
        assert(sortedArray == t['output'])
        assert(invCount == t['result'])
        
