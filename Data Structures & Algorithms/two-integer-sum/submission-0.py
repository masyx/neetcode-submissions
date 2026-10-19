class Solution:
    # nums = [3,4,5,6], target = 7
    # 1. track seen numbers in a dict: O(n) time, O(n) space
    # 2. sort first and then use two pointers to find the traget: O(n log n) time, O(1) space
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            possible_match = target - num
            if possible_match in seen:
                return [seen[possible_match], i]
            seen[num] = i
        
        return None