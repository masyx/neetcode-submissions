class Solution:
    # [1,2,3]
    def missingNumber(self, nums: List[int]) -> int:
        # 1 xor 1 = 0
        
        # num = 2
        #      [0 2]
        # range 0 1 
        num = len(nums)

        for i in range(len(nums)):
            num = num ^ nums[i] ^ i

        return num
