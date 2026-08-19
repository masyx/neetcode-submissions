"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    # intervals = [(0,40),(5,10),(5,10),(15,30),(20,30)] room = 4
    # if the start of the meeting is the same or more the the end of the previous meeting
    # heap: 10, 30, 20, 40
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        sorted_intervals = sorted(intervals, key=lambda interval: interval.start) # O(n log n) time
        
        heap = []
        for interval in sorted_intervals:
        
            if heap and interval.start >= heap[0]: # if the start of the new meeting is later(>) or at the same time(=) 
            # as the end of the earliest meeting endtime means that room can be REUSED
                heapq.heappop(heap)

            heapq.heappush(heap, interval.end)

        return len(heap)