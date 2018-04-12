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
        def tree_paths(r, ans, path):
            if not r.left and not r.right:
                ans.append(path)
            if r.left:
                tree_paths(r.left, ans, path+'->'+str(r.left.val))
            if r.right:
                tree_paths(r.right, ans, path+'->'+str(r.right.val))
        
        
        if not root: return []
        
        ans = []       
        tree_paths(root, ans, str(root.val))
        return ans