# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Case 1: Both p and q are smaller than the current root.
        # The LCA must be in the left subtree.
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # Case 2: Both p and q are larger than the current root.
        # The LCA must be in the right subtree.
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        # Case 3: We found the split.
        # Either one is on the left and one on the right, OR
        # the current root is actually p or q itself.
        else:
            return root