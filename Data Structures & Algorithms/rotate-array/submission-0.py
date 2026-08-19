class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # len = 8, k = 4, mod(remainder) is 0
        # [1 2 3 4] k = 2
        #           0 1 2 3
        # reverse: [4 3 2 1]
        #
        # result:
        #   1) reverse from 0 to k [3 4 2 1]
        #   2) reverse from k to len(nums) [3 4 1 2]
        n = len(nums)
        k %= n
        def reverse(arr, l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        nums.reverse()
        # reverse the first portion
        reverse(nums, 0, k - 1)
        # reverse the second portion
        reverse(nums, k, n - 1)