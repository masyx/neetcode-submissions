class Solution:
    def isBalanced(self, root) -> bool:
        def height_or_fail(root):
            if not root:
                return 0
            
            l_h = height_or_fail(root.left)
            if l_h == -1:
                return -1
            
            r_h = height_or_fail(root.right)
            if r_h == -1:
                return -1
            
            if abs(l_h - r_h) > 1:
                return -1
            return max(l_h, r_h) + 1
            
        res = height_or_fail(root)
        return res != -1