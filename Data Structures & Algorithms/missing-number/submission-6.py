class Solution:
    #i 0 1 2
    # [1,2,3]
    # n = 3
    # 
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        for i in range(n):
            if i != nums[i]:
                return i
        return n