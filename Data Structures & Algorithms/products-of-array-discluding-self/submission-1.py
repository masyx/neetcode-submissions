class Solution:
    # i:0  1  2  3
    # [ 1, 2, 4, 6] nums
    # [ 1, 1, 2, 8] left_product
    # [48,24, 6, 1] right_product

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        left_product = [1] * len(nums)
        right_product = [1] * len(nums)

        for i in range(len(nums) - 1):
            left_product[i + 1] = nums[i] * left_product[i]

        for i in range(len(nums) - 1, 0, -1):
            right_product[i - 1] = nums[i] * right_product[i]

        for i in range(len(nums)):
            output[i] = left_product[i] * right_product[i]

        return output