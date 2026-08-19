from collections import Counter, deque
import heapq
from typing import List



class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # ["A","A","A","B","C"] n = 3, cycles = 9
        # ABC_A___A
        # store tasks count in a heap to always try to run the most frequent task
        # after the task was executed put it back into the queue with calculated availability time IF it wasn't exhousted(count > 0)
        # for every cycle check if the task in queue cooled down and can be moved to the heap

        counts = Counter(tasks)
        max_heap = [(-count, task) for task, count in counts.items()]
        heapq.heapify(max_heap)
        q = deque() # cooldown queue to store tasks that are cooling down (task, available_at)

        cycles = 0
        while len(max_heap) > 0 or len(q) > 0:
            cycles += 1

            if len(q) > 0 and q[0][1] == cycles:
                heapq.heappush(max_heap, q.popleft()[0]) # push the cooled down task back onto heap

            if len(max_heap) > 0:
                count, task = heapq.heappop(max_heap)
                count += 1
                if count != 0:
                    available_at = cycles + n + 1
                    q.append(((count, task), available_at))

        return cycles
