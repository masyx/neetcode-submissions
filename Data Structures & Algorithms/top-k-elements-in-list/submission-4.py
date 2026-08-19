import heapq

class Solution:
    # iterate nums and count distinct digits
    # iterate counter and put the k most frequent numbers into a hip
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        hip = []

        for num, count in counts.items():
            if len(hip) < k:
                heapq.heappush(hip, (count, num))
            else:
                if count > hip[0][0]:
                    heapq.heappushpop(hip, (count, num))

        return [num for count, num in hip]