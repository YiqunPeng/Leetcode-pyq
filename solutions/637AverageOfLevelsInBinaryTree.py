# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root: return []
        
        ans = [float(root.val)]
        nodes = [root]
        next = []
        
        while nodes:
            for node in nodes:
                if node.left: next.append(node.left)
                if node.right: next.append(node.right)
            nodes = next
            next = []
            if not nodes: break
            values = [item.val for item in nodes]
            ans.append(float(sum(values)) / len(values))
        
        return ans