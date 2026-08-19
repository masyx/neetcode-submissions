class Solution:

    # n = number of stairs
    # ways(n) = ways(n - 1) + ways(n - 2)
    # n = 4
    # i:      1 2 3 4 5   
    # three = 1,2 3 5
    # one =   1,1 2 3
    # two =   1,2 3 5
    
    def climbStairs(self, n: int) -> int:
        one, two = 0, 1
        for i in range(n):
            third = one + two
            one = two
            two = third
        return two
        