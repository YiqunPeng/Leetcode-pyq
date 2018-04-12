# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        stack = []
        mode = 'push'
        
        if not root: return ans
        
        stack.append(root)
        while stack:
            node = stack[-1]
            if mode == 'push':
                while node.left:
                    stack.append(node.left)
                    node = node.left
                mode = 'pop'
            
            ans.append(node.val)
            stack.pop(-1)
            if node.right:
                stack.append(node.right)
                mode = 'push'
        
        return ans
            
        