class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket_array = [[] for _ in range(len(nums) + 1)]
    
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            
        for num, count in counts.items():
            bucket_array[count].append(num)
            
        res = []
        for i in range(len(bucket_array) - 1, 0, -1):
            for num in bucket_array[i]:
                res.append(num)
                if len(res) == k:
                    return res