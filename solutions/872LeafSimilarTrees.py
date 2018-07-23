# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaf1, leaf2 = [], []
        
        def dfs(root, leaf):
            if not root: return
            if not root.left and not root.right:
                leaf.append(root.val)
                return 
            if root.left: dfs(root.left, leaf)
            if root.right: dfs(root.right, leaf)

        dfs(root1, leaf1)
        dfs(root2, leaf2)
        
        return leaf1 == leaf2
