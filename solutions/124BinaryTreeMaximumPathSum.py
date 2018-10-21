# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __init__(self):
        self.ans = -sys.maxsize
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def postorder(node):
            if not node.left and not node.right:
                self.ans = max(self.ans, node.val)
                return node.val
            
            l, r = 0, 0
            if node.left: l = postorder(node.left)
            if node.right: r = postorder(node.right)
                
            s = max(0, l) + max(0, r) + node.val
            self.ans = max(self.ans, s)
            
            return max(l + node.val, r + node.val, node.val)
            
        
        postorder(root)
        return self.ans