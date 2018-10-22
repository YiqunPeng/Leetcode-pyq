# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def view(node, depth):
            if not node: return
            
            if len(ans) == depth:
                ans.append(node.val)
                
            view(node.right, depth + 1)
            view(node.left, depth + 1)
        
        
        ans = []
        view(root, 0)
        return ans