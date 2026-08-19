"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    # [(1,5),(2,6),(3,7),(4,8),(5,9)]
    # 6, 7, 8, 9 
    # O(n log n ) time | O(n) space
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda interval: interval.start) # n log n

        rooms = []
        for interval in intervals:
            if not rooms or interval.start < rooms[0]:
                heapq.heappush(rooms, interval.end)
            else:
                heapq.heappushpop(rooms, interval.end)
        return len(rooms)