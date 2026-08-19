class Solution:
    def isBalanced(self, root) -> bool:
        def isBalancedHelper(node):
            if not node:
                return 0  # height

            l_h = isBalancedHelper(node.left)
            if l_h is False:  # propagate failure explicitly
                return False

            r_h = isBalancedHelper(node.right)
            if r_h is False:
                return False

            if abs(l_h - r_h) > 1:
                return False

            return max(l_h, r_h) + 1  # be consistent: height + 1 here

        res = isBalancedHelper(root)
        # empty tree should be True; res can be 0 (height), >=1 (height), or False (unbalanced)
        return res is not False