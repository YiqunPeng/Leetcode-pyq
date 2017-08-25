# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        
        def post_traversal(root):
            if not root.left and not root.right:
                return root.val
            l, r = 0, 0
            if root.left:
                l = post_traversal(root.left)
            if root.right:
                r = post_traversal(root.right)
            self.ans += abs(l - r)
            return root.val + l + r
                   
        if not root: return 0
        post_traversal(root)
        return self.ans
    