# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # recursive
    # time: O(n^2)
    # space: O(n)
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder: return None

        root = TreeNode(preorder[0])
        pos = inorder.index(preorder[0])

        root.right = self.buildTree(preorder[pos+1:], inorder[pos+1:])
        root.left = self.buildTree(preorder[1:pos+1], inorder[0:pos])

        return root