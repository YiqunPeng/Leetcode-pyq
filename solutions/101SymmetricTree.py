# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        
        return self.is_symmetric(root.left, root.right)
    
    def is_symmetric(self, l, r):
        if not l and not r: return True
        if (not l and r) or (not r and l): return False
        if l.val != r.val: return False
        
        if l.left and l.right:
            return self.is_symmetric(l.left, r.right) and self.is_symmetric(l.right, r.left)
        elif l.left and not l.right:
            return self.is_symmetric(l.left, r.right) and not r.left
        elif not l.left and l.right:
            return not r.right and self.is_symmetric(l.right, r.left)
        else:
