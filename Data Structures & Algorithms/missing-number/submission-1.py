class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_possible_number = len(nums)
        res = max_possible_number
        for i, num in enumerate(nums):
            res = res ^ i ^ num
        return res