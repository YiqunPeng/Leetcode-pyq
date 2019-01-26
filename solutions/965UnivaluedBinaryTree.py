# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root, val = None):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        if val is None: val = root.val    
        if val != root.val: return False
        
        return self.isUnivalTree(root.left, val) and self.isUnivalTree(root.right, val)