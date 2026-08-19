class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(1, len(res)):
            j = i
            count = 0
            while j != 0:
                j = j & (j - 1)
                count += 1
            res[i] = count
        return res