# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def dfs(root, level, res):
            if root:
                if len(res) < level + 1:
                    res.insert(0, [])
                res[-(level+1)].append(root.val)
                dfs(root.left, level+1, res)
                dfs(root.right, level+1, res)

        res = []
        dfs(root, 0, res)
        return res
        