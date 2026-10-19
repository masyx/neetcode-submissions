class Solution:
    # nums=[3,2,3] target=6
    # 2 3 3
    # 1. track seen numbers in a dict: O(n) time, O(n) space
    # 2. sort first and then use two pointers to find the traget: O(n log n) time, O(1) space
    # !!!!!!! SORTING DOESN"T WORK DAmbaSS, we need to return indeces
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i

        return None