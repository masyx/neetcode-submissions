class Solution:
    def reverse(self, n: int) -> int:
        MAX_INT = 2 ** 31 - 1 # 2147483647
        MIN_INT = -2 ** 31 # 2147483648
        res = 0
        while n != 0:
            pop = int(math.fmod(n, 10))
            n = int(n / 10)
            
            if (res > MAX_INT // 10 - pop) or (res == MAX_INT // 10 and pop == 7):
                return 0 
            elif (res < MIN_INT // 10 - pop) or (res == MIN_INT // 10 and pop == 8):
                return 0
            # if (res * 10 + pop) > MAX_INT
            
            res = res * 10 + pop
            
        return res