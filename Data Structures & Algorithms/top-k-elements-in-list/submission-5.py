import heapq

class Solution:
    # 1:5, 5:6, 7:8
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        heap = []

        for num, count in freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, num))
            elif count > heap[0][0]:
                heapq.heappushpop(heap, (count, num))

        return [num for count, num in heap]
        
        