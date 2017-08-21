# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p and not q) or (not p and q):
            return False
        if not q and not p:
            return True
        if (p.val == q.val) and ((not p.left and not q.left) or (p.left and q.left and self.isSameTree(p.left, q.left))) and ((not p.right and not q.right) or (p.right and q.right and self.isSameTree(p.right, q.right))):
            return True
        return False
        