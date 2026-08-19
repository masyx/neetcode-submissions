class Solution:
    # Input: stones = [2,7,4,1,8,1]
    # Output: 1
    # 8 7 4 2 1 1; 8 - 7 = 1
    # 42111; 4-2 = 2
    # 2111; 2 - 1 = 1
    # 111: 1 == 1
    # 1
    
    # O(n log n) time | O(1) space
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones) # O(n) time
        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            diff = x - y
            if diff:
                heapq.heappush(stones,-diff)
        return -stones[0] if stones else 0
    
    
        