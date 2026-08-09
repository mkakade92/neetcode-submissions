"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        

        if len(intervals)<=1:
            return len(intervals)

        intervals.sort(key=lambda x : x.start)

        pq = []
        heapq.heappush(pq,intervals[0].end)

        for interval in intervals[1:]:
            end = pq[0]
            if interval.start>=end:
                heapq.heappop(pq)
            heapq.heappush(pq,interval.end)
        return len(pq)
