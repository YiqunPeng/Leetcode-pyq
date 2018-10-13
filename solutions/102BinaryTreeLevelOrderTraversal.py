# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []    
        ans = []
        
        lvl = [root]
        while lvl:
            ans.append([n.val for node in lvl])
            nxt = []
            for node in lvl:
                if node.left: nxt.append(node.left)
                if node.right: nxt.append(node.right)
            lvl = nxt
        
        return ans