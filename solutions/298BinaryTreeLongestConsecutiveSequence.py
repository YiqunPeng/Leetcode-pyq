# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # dfs, post order, no global variable
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, ans):
            if not node: 
                return 0, 0
            if not node.left and not node.right:
                return 1, max(ans, 1)
            
            res = 1
            
            left, la = dfs(node.left, ans)
            right, ra = dfs(node.right, ans)
            
            if node.left and node.left.val == node.val + 1:
                res = max(left + 1, res)
            if node.right and node.right.val == node.val + 1:
                res = max(right + 1, res)
            
            return res, max(ans, la, ra, res)
                
        return dfs(root, 0)[1]

    # dfs, post order traverse, use global variable
    # def __init__(self):
    #     self.ans = 0

    # def longestConsecutive(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     def dfs(node):
    #         if not node: 
    #             return 0
    #         if not node.left and not node.right:
    #             self.ans = max(self.ans, 1)
    #             return 1
            
    #         res = 1
            
    #         left = dfs(node.left)
    #         right = dfs(node.right)
            
    #         if node.left and node.left.val == node.val + 1:
    #             res = max(left + 1, res)
    #         if node.right and node.right.val == node.val + 1:
    #             res = max(right + 1, res)
            
    #         self.ans = max(self.ans, res)
    #         return res
                
        
    #     dfs(root)
    #     return self.ans
        