# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

from heapq import heappop as hpop, heappush as hpush
class Solution:
    def minMeetingRooms(self, intervals: 'List[Interval]') -> 'int':
        if not intervals: return 0
        rooms = []
        intervals.sort(key = lambda x: x.start) # In-place sort is more memory efficient
        hpush(rooms,intervals[0].end)
        for i in intervals[1:]:
            if rooms[0] <= i.start:
                hpop(rooms)
            hpush(rooms, i.end)
        return len(rooms)
