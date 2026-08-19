class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF #2147483647

        while b != 0:
            res = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a = res
            b = carry 
        
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)
