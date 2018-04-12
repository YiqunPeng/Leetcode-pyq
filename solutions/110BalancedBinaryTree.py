# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def depth(r):
            if not r:
                return 0
            if not r.left and not r.right:
                return 1
            return max(depth(r.left), depth(r.right)) + 1
        
        
        def balanced_tree(r):
            if not r or (not r.left and not r.right):
                return True
            left, right = 0, 0
            if r.right:
                right = depth(r.right)
            if r.left:
                left = depth(r.left)
            if abs(right-left) > 1:
                return False
            else:
                return balanced_tree(r.left) and balanced_tree(r.left) 
        
        
        if not root: return True        
        return balanced_tree(root)