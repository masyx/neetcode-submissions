from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # ["A","A","A","B","C"], n = 3, 9 cycles
        # 12345678910
        # ABC_A___A
        # I need to execute the most frequent tasks first
        # After the task runs, I move it to a cooldown queue with calculated availability time
        # repeat untill the queue or heap is empty

        #counts = Counter(tasks)
        counts = {}
        for task in tasks:
            counts[task] = counts.get(task, 0) + 1

        max_heap = [-count for task, count in counts.items()]
        heapq.heapify(max_heap)

        q = deque()
        cycles = 0

        while max_heap or q:
            cycles += 1
            if q and q[0][0] == cycles:
                heapq.heappush(max_heap, q.popleft()[1])

            if max_heap:
                curr_task = heapq.heappop(max_heap)
                curr_task += 1 # task executed

                if curr_task < 0:
                    q.append((cycles + n + 1, curr_task))
        return cycles
            


