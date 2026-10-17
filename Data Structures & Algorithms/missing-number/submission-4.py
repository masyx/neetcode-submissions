class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        l = len(nums)
        
        if nums[0] != 0:
            return 0
        if nums[-1] != l:
            return l

        for i in range(1, l):
            curr_num = nums[i]
            diff = nums[i] - nums[i - 1]
            if diff > 1:
                return nums[i] - 1
