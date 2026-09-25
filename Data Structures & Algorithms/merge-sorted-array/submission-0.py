class Solution:
    #
    #
    # i         0  1  2  3 4 5
    #                      v
    #                v
    # nums1 = [1, 2,10,40,20,10], m = 4
    #              v
    # nums2 = [1,2], n = 2
    #
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()
        