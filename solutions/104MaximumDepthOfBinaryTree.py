# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object): 
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 0
        
        if root == None:
            return ans
        
        nodes = [root]
        while len(nodes) != 0:
            child_nodes = []
            for node in nodes:
                if node and node.left:
                    child_nodes.append(node.left)
                if node and node.right:
                    child_nodes.append(node.right)
            nodes = child_nodes
            ans += 1
        
        return ans
        