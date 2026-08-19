#  0 1 2 3 4 5
# [5,6,7,2,3,4]
#
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[-1] > nums[0]:
            return nums[0]

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid - 1