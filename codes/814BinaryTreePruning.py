# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(node):
            if not node.left and not node.right and node.val == 0:
                return -1
            if node.left and dfs(node.left) == -1:
                node.left = None
            if node.right and dfs(node.right) == -1:
                node.right = None
            if not node.left and not node.right and node.val == 0:
                return -1
            
        
        if not root: return None
        
        dfs(root)
        
        return root