# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        while root:
            if root.val == val: 
                return root
            elif root.val > val:
                if root.left:
                    root = root.left
                else:
                    return None
            else:
                if root.right:
                    root = root.right
                else:
                    return None            
            