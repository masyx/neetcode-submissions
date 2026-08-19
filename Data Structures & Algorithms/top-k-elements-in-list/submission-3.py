class Solution:
    # i       0 1 2 3 4 5
    # nums = [1,2,2,3,3,3], k = 2
    # freq: 1-1; 2-2; 3-3
    # sort by values and return k first keys
    # O(1) time | O(n) space
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        # [1-1; 2-2; 3-3]
        res_list = sorted(freq.items(), key=lambda kv: kv[1], reverse=True)
        res = []
        for i in range(k):
            res.append(res_list[i][0])
        return res
