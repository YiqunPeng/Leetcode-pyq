# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def search(node, val):
            if node.val < val:
                if node.right:
                    search(node.right, val)
                else:
                    node.right = TreeNode(val)
            else:
                if node.left:
                    search(node.left, val)
                else:
                    node.left = TreeNode(val)
        
        
        if not root:
            root = TreeNode(val)
        else:
            search(root, val)
        
        return root       