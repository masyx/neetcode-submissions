class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if nums[r] > nums[l] or len(nums) == 1:
            return nums[l]
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] < nums[mid - 1]:
                return nums[mid]

            if nums[mid] > nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        