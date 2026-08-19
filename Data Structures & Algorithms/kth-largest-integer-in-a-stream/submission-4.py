import heapq

class KthLargest:
    # [3, [1, 2, 3, 3]]; heap [2 3 3]
    # add 3; [3 3 3] -> 3
    # add 5; [3 3 5] -> 3
    # add 6; [3 5 6] -> 3
    # add 7; [5 6 7] -> 5
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        for num in nums:
            if len(self.heap) < self.k:
                heapq.heappush(self.heap, num)
            elif num > self.heap[0]:
                heapq.heappushpop(self.heap, num)



    # [3]; k = 4; add 6 -> if len(heap) < k: heappush
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]
        
