# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root: return []
        
        ans = []
        level = [root]
        
        while level:
            avg = sum([node.val for node in level]) / len(level)
            ans.append(avg)
            
            nxt = []
            for node in level:
                if node.left: nxt.append(node.left)
                if node.right: nxt.append(node.right)
            level = nxt
        
        return ans