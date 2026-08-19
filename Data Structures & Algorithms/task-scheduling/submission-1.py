from typing import List
import heapq
from collections import deque

class Solution:
    # tasks = ["A","A","A","B","C"]; n = 3; res = 9 -> abc_a___a
    # max_heap: [-1]
    # time: 9
    # cnt: 0
    # queue: []
    # 
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        max_heap = [-count for count in freq if count > 0]
        heapq.heapify(max_heap)
        time = 0
        q = deque()

        while max_heap or q:
            time += 1
            
            if max_heap:
                cnt = heapq.heappop(max_heap) + 1
                if cnt:
                    q.append((cnt, time + n)) # (task_count_left, time_becomes_available)
            else:
                time = q[0][1] # set the clock to the availability time of the first task in the queue

            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0]) # push task_count_left from the queue
        
        return time