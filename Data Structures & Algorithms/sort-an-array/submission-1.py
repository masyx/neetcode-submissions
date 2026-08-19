class Solution:
    #    0 1 2 3 4 5 6 7
    #  [10,9,1,1,1,2,3,1]
    #
    #
    def sortArray(self, nums: List[int]) -> List[int]:
        is_sorted = False
        while not is_sorted:
            is_sorted = True
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    is_sorted = False
        return nums