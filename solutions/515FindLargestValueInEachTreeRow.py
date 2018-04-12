# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        
        ans = [root.val]
        nodes = [root]
        next = []
        
        while nodes:
            for node in nodes:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            if not next: 
                nodes = next
                break
            values = [item.val for item in next]
            ans.append(max(values))
            nodes = next
            next = []
        
        return ans