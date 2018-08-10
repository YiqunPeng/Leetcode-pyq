# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # dfs
    # time: O(n)
    # space: O(1)
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, max_b):
            if not node: return 0, 0
            if not node.left and not node.right: return 0, 0
            
            ls, lb = dfs(node.left, max_b)
            rs, rb = dfs(node.right, max_b)
            
            res_s, res_b = 0, 0
            if node.left and node.val == node.left.val:
                res_s = ls + 1
                res_b += ls + 1
            if node.right and node.val == node.right.val:
                res_s = max(res_s, rs + 1)
                res_b += rs + 1
            res_b = max(res_b, max_b, lb, rb)
            
            return res_s, res_b

        return max(dfs(root, 0))
        