class Solution:
    # Bubble sort: O(n^2) time, O(1) space
    #  0 1 2 3 4 5 6 7
    # [10,9,1,1,1,2,3,1]
    # [9,1,1,1,2,3,1,10]
    # [1,1,1,2,3,1,9,10]
    # [1,1,1,2,1,3,9,10]
    # [1,1,1,1,2,3,9,10]
    # [1,1,1,1,2,3,9,10] no swaps


    def sortArray(self, nums: List[int]) -> List[int]:
        # bubble sort
        n = len(nums)
        for i in range(n - 1):
            swapped = False
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True
            if not swapped:
                break
        return nums