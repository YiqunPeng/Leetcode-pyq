# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root
        self.dfs(root, d-2, v)
        return root
        
    def dfs(self, root, d, v):
        if d == 0: 
            self.add(root, v)
            return
        if root.left:
            self.dfs(root.left, d-1, v)
        if root.right:
            self.dfs(root.right, d-1, v)
    
    def add(self, root, v):
        new_left = TreeNode(v)
        new_right = TreeNode(v)
        if root.left:
            new_left.left = root.left
        if root.right:          
            new_right.right = root.right
        root.left = new_left
        root.right = new_right