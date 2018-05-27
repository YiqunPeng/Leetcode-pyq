# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodes = []
        
        
        def is_unival(n):
            if not n: 
                return True
            l_unival = not n.left or is_unival(n.left)
            r_unival = not n.right or is_unival(n.right)
            
            l_val = not n.left or n.left.val == n.val
            r_val = not n.right or n.right.val == n.val
            
            if l_unival and r_unival and l_val and r_val:
                nodes.append(n)
                return True

            
        is_unival(root)     
        return len(nodes)