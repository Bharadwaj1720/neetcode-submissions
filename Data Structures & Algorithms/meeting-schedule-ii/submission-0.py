"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, Intervals: List[Interval]) -> int:
        time=0
        count=0
        intervals=[]
        for i in Intervals:
            intervals.append((i.start,i.end))
        intervals.sort()
        heap=[]
        for i in intervals:
            while len(heap)!=0 and heap[0]<=i[0]:
                heapq.heappop(heap)
            heapq.heappush(heap,i[1])
            count=max(count,len(heap))
        return count
        