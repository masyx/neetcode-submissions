# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #      1
    #     2 3
    #    4   5
    #   6     7
    #
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs_balanced(node):
            if not node:
                return 0

            lh = dfs_balanced(node.left)
            if lh == -1:
                return -1
            rh = dfs_balanced(node.right)
            if rh == -1:
                return -1

            if abs(lh - rh) > 1:
                return -1
            
            return 1 + max(lh, rh)
        return dfs_balanced(root) != -1



        