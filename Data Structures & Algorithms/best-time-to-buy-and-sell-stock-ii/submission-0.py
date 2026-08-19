class Solution:
    # idx       0 1 2 3 4 5
    # prices = [7,1,5,3,6,4]                 if prices[i] > prices[i-1]:     else: 
    # res = [4, 3] sum = 40, expected = 39
    def maxProfit(self, prices: List[int]) -> int:
        res = []
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                res.append(prices[i] - prices[i - 1])
        return sum(res)

        