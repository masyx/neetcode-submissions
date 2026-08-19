class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        sorted_keys = sorted(counts, key=lambda k: counts[k], reverse=True)
        return sorted_keys[0:k]
        