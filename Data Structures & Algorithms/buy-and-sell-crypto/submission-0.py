class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float('inf')
        biggest = float('-inf')
        profit = 0
        for price in prices:
            if price < lowest:
                biggest  = price
                lowest = price
            biggest = max(biggest, price)
            profit = max(biggest - lowest, profit)
        return profit  