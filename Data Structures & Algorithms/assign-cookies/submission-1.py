class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        #g=[10,9,8,7] s=[5,6,7,8]
        #g 78910  s 5678
        
        res = 0

        g.sort()
        s.sort()

        i = 0
        j = 0

        # i = 0
        # j = 0
        # res = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                res += 1
                i += 1
                j += 1
            else:
                j += 1
        
        return res

            
        