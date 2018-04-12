# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return root
        
        self.invert(root)
        return root
    
    def invert(self, root):
        temp = root.left
        root.left = root.right
        root.right = temp
        
        if root.left: self.invert(root.left)
        if root.right: self.invert(root.right)