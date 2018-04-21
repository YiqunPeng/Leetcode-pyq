# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def depth(node, d):
            if not node:
                return d - 1
            if not node.left and not node.right:
                return d
            return max(depth(node.left, d+1), depth(node.right, d+1))
    
        return depth(root, 1)