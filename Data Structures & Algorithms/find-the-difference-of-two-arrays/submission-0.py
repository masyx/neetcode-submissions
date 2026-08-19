class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        # Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
        #Output: [[3],[]]

        # 1 2 3   1 2
        # res[[3], []]


        # Input: nums1 = [1,2,3,5], nums2 = [2,4,6]
        # Output: [[1,3,5],[4,6]]
        # 1235 246
        #
        nums1_set = set(nums1) # n
        nums2_set = set(nums2) # m

        res = [[],[]]

        for num in nums1_set:
            if num not in nums2_set: # O(1) * n
                res[0].append(num)

        for num in nums2_set:
            if num not in nums1_set: # O(1) * m
                res[1].append(num)
        
        return res
        