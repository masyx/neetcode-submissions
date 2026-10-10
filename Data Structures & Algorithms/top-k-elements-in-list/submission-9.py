from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 6 3 4 2 8 1
        # 4 6 8

        freq = Counter(nums)
        heap = []

        for number, count in freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, number)) 
            elif count > heap[0][0]:
                heapq.heappushpop(heap, (count, number))

        return [number for count, number in heap]




