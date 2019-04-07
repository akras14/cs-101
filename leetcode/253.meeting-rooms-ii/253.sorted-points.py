# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals: 'List[Interval]') -> 'int':
        START = 1 
        END = 0 # Sort by placing end first
        points = []
        for i in intervals:
            points.append((i.start,START))
            points.append((i.end,END))
        points = sorted(points)
        maxrooms = 0
        currooms = 0
        for p in points:
            ptime, ptype = p
            if ptype == END:
                currooms -= 1
            else:
                currooms += 1
                maxrooms = max(currooms, maxrooms)
        return maxrooms
