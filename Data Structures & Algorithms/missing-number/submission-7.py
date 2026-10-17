class Solution:
    #set: 0 1 2
    #     [0,2]
    # n = 3
    # 
    def missingNumber(self, nums: List[int]) -> int:
        complete_set = set()
        for i in range(len(nums) + 1):
            complete_set.add(i)

        for num in complete_set:
            if num not in nums:
                return num

        return None