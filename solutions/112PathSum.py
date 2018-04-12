# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: return False
              
        return self.path_sum(root, 0, sum)
    
    def path_sum(self, r, v, sum):
        if not r.left and not r.right and r.val + v == sum:
            return True
        else:
            left = self.path_sum(r.left, v+r.val, sum) if r.left else False
            right = self.path_sum(r.right, v+r.val, sum) if r.right else False
            return left or right