class Solution:
    #set: 0 1 2
    #     [0,2]
    # n = 3
    # 
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)

        for i in range(len(nums) + 1):
            if i not in num_set:
                return i

        return None