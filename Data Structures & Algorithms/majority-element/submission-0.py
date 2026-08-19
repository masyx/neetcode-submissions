
class Solution:
    # 5:4, 1:3
    #
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
            if freq[num] > len(nums) / 2:
                return num
