# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        
        ans = []
        nodes = [root]
        while nodes:
            top = nodes.pop(-1)
            ans.append(top.val)
            if top.right:
                nodes.append(top.right)
            if top.left:
                nodes.append(top.left)
        
        return ans