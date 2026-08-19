class Solution:
    #     0 1 2 3 4 5 
    #   [10,9,1,2,3,1]
    #   [10,9,1]         [2,3,1]
    #   [10,9] [1]       [2,3] [1]
    #   [10] [9]         [2] [3]
    #   merge
    #   [9 10]           [2 3]
    #           l               r
    #   [1 9 10]         [1 2 3]
    #   [1 1 2 3 9 10]
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left_arr, right_arr):
            left_ptr = 0
            right_ptr = 0

            res_arr = []
            while left_ptr < len(left_arr) and right_ptr < len(right_arr):
                if left_arr[left_ptr] < right_arr[right_ptr]:
                    res_arr.append(left_arr[left_ptr])
                    left_ptr += 1
                else:
                    res_arr.append(right_arr[right_ptr])
                    right_ptr += 1

            while left_ptr < len(left_arr):
                res_arr.append(left_arr[left_ptr])
                left_ptr += 1

            while right_ptr < len(right_arr):
                res_arr.append(right_arr[right_ptr])
                right_ptr += 1

            return res_arr

        if len(nums) == 1:
            return nums

        mid = len(nums) // 2
        left_arr = self.sortArray(nums[:mid])
        right_arr = self.sortArray(nums[mid:])

        sorted_arr = merge(left_arr, right_arr)
        return sorted_arr




