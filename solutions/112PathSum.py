# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def dfs(node, remain):
            if not node: return False
                
            if not node.left and not node.right:
                if node.val == remain:
                    return True
                else:
                    return False
            
            res = dfs(node.left, remain - node.val)
            if res: return True
        
            res = dfs(node.right, remain - node.val)
            return res
        
        
        if not root: return False
        
        return dfs(root, sum)