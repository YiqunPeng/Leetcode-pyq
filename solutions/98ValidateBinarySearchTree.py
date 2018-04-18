# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValid(self, root, min_v, max_v):
        if not root: return True
        if root.val <= min_v or root.val >= max_v: return False
        return self.isValid(root.left, min_v, root.val) and self.isValid(root.right, root.val, max_v)
        
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.isValid(root, -sys.maxsize, sys.maxsize)
