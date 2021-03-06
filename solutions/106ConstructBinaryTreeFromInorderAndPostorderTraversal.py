# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder: return None
        
        root = TreeNode(postorder[-1])
        pos = inorder.index(postorder[-1])
        
        root.right = self.buildTree(inorder[pos+1:], postorder[pos:-1])
        root.left = self.buildTree(inorder[0:pos], postorder[0:pos])
    
        return root