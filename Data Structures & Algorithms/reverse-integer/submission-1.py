class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = 2**31 # leaving it positive, because operating with x = abs(x) 
        
        sign = 1 if x >= 0 else -1
        res = 0
        x = abs(x)
        
        while x != 0:
            x, pop = divmod(x, 10)
            
            if sign == 1 and res > (MAX_INT - pop) // 10:
                return 0
            elif sign == -1 and res > (MIN_INT - pop) // 10:
                return 0
                
            res = res * 10 + pop
        return sign * res      