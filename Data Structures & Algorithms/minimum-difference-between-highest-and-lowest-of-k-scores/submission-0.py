class Solution:
    # Input: nums = [2,5,3,1,6,3], k = 3   brute force: O(n^k * k)
    # Output: 1
    #          0 1 2 3 4 5
    # sorted: [1,2,3,3,5,6] O(n log n)
    # 1479 k=2
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if not nums:
            return None
        nums.sort()
        diff = float("inf") 
        for i in range(len(nums) - k + 1):
            diff = min(diff, nums[i + k - 1] - nums[i])
        return diff