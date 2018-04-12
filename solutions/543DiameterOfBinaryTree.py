# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(r):
            left, right, root = [0,0], [0,0], [0,0]
            if r.left:
                left = dfs(r.left)
            if r.right:
                right = dfs(r.right)
            root[1] = max(left[1], right[1]) + 1
            root[0] = max(left[0], right[0], left[1]+right[1])
            return root            
        
        if not root: return 0
        
        ans = dfs(root)        
        return ans[0]