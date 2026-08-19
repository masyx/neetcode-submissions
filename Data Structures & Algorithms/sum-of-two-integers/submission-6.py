class Solution:
    # a 101
    # b 011
    # sum = 110
    # carry = 001 << 1 = 010
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 2**31 #0x7FFFFFFF
        while b != 0:
            sum_ = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a = sum_
            b = carry
        return a if a <= max_int else ~(a ^ mask)

        