from collections import Counter
import heapq

class Solution:
    # appraoch 1 -> count dict and sort: Time: O(m log m) where m is the number of unique elements
    # in the array, O(m) space

    # appraoch 2 -> count dict, O(k) to iterate over dict and store the k most repeated elements in a heap.
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []

        for key, count in counts.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, key))
            elif count > heap[0][0]:
                heapq.heappushpop(heap, (count, key))
        
        return [key for count, key in heap]