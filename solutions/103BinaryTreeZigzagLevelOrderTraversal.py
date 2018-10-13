# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        
        ans = []
        depth = 1
        
        lvl = [root]
        while lvl:
            if depth % 2 == 1:
                ans.append([node.val for node in lvl])
            else:
                ans.append([node.val for node in lvl][::-1])
            depth += 1
            
            nxt = []
            for node in lvl:
                if node.left: nxt.append(node.left)
                if node.right: nxt.append(node.right)
            lvl = nxt
        
        return ans