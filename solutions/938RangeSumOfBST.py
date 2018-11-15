# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        stack = []
        ans = 0
        
        while stack or root:
            if root:    
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if root.val > R: return ans
                if L <= root.val <= R: ans += root.val
                root = root.right
        
        return ans