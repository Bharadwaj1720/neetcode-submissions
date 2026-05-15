"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self,Intervals: List[Interval]) -> bool:
        intervals=[]
        for i in Intervals:
            intervals.append((i.start,i.end))
        intervals.sort()
        for i in range(len(intervals)-1):
            if intervals[i][1]>intervals[i+1][0]:
                return False
        return True
