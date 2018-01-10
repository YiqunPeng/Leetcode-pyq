# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return -1
        if not root.left and not root.right: return -1
        
        f_min, s_min = root.val, sys.maxsize
        nodes = [root.left, root.right]
        
        while nodes:
            next_nodes = []
            for n in nodes:
                if n.right:
                    next_nodes.append(n.right)
                    next_nodes.append(n.left)
                if n.val > f_min and n.val < s_min:
                    s_min = n.val
            nodes = next_nodes
        
        if s_min != sys.maxsize:
            return s_min
        else:
            return -1
            
        
        
        