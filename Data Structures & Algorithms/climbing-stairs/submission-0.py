class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(curr):
            if curr == n:
                return 1
            elif curr > n:
                return 0
            l = dfs(curr + 1)
            r = dfs(curr + 2)
            return l + r
        
        return dfs(0)
        