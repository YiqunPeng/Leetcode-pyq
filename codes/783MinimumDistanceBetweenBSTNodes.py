# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def preorder(values, root):
            if not root: return 
            
            preorder(values, root.left)
            values.append(root.val)
            preorder(values, root.right)
          
        
        values = []
        preorder(values, root)
        diff = []
        for i in range(len(values)-1):
            diff.append(values[i+1]-values[i])
        return min(diff)