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
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, max_b):
            if not node: return 0, max_b
            if not node.left and not node.right:
                return node.val, max(node.val, max_b)
            
            ls, lb = dfs(node.left, max_b)
            rs, rb = dfs(node.right, max_b)
            
            res_s = max(0, ls, rs) + node.val
            res_b = max((max(0, ls) + max(0, rs) + node.val), lb, rb)
            
            return res_s, res_b
        
        return max(dfs(root, -sys.maxsize))