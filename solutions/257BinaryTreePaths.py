# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def tree_paths(r, path):
            if not r.left and not r.right:
                ans.append(path)
            if r.left:
                tree_paths(r.left, path + '->' + str(r.left.val))
            if r.right:
                tree_paths(r.right, path + '->' + str(r.right.val))
        
        
        if not root: return []
        ans = []       
        tree_paths(root, str(root.val))
        return ans