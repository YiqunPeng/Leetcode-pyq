# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodes = [root]
        next_layer_nodes = []
        ans = root.val
        
        if root.left: 
            next_layer_nodes.append(root.left)
        if root.right:
            next_layer_nodes.append(root.right)
            
        while len(next_layer_nodes) != 0:
            ans = next_layer_nodes[0].val
            nodes = next_layer_nodes
            next_layer_nodes = []
            for node in nodes:
                if node.left:
                    next_layer_nodes.append(node.left)
                if node.right:
                    next_layer_nodes.append(node.right)       
            
        return ans