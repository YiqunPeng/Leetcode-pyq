# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        right = self.sumOfLeftLeaves(root.right) if root.right and not self.is_leaf(root.right) else 0

        if root.left and self.is_leaf(root.left):
            return root.left.val + right
        else:
            left = self.sumOfLeftLeaves(root.left) if root.left else 0
            return left + right
        
    def is_leaf(self, node):
        if not node:
            return False
        return not (node.left or node.right)