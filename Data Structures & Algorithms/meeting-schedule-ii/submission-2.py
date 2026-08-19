"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    # intervals = [(0,40),(5,10),(15,20)]
    # intervals=[(25,579),(218,918),(1281,1307),(623,1320),(685,1353),(1308,1358)] 3
    # heap: 0
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda meeting: meeting.start)
        heap = []
        for meeting in intervals:
            if heap and meeting.start >= heap[0]:
                heapq.heappushpop(heap, meeting.end)
            else:
                heapq.heappush(heap, meeting.end)

        return len(heap)