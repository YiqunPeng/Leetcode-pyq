# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def dfs(node, path, curr):
            if not node.left and not node.right and curr == sum:
                ans.append(path[:])
            
            if node.left:
                dfs(node.left, path + [node.left.val], curr + node.left.val)
            if node.right:
                dfs(node.right, path + [node.right.val], curr + node.right.val)
        
        
        if not root: return []
        ans = []
        dfs(root, [root.val], root.val)
        return ans
        