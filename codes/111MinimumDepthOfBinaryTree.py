# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        
        nodes = [root]
        ans = 1
        
        while True:
            next_depth = []
            for node in nodes:
                if not node.left and not node.right:
                   return ans
                else:
                    if node.left: next_depth.append(node.left)
                    if node.right: next_depth.append(node.right)
            nodes = next_depth
            ans += 1