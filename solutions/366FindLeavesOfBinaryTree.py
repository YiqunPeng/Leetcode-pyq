# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def is_leaf(node):
            return not node.right and not node.left
        
        def dfs(l, node):
            if not node.left and not node.right:
                return
            if node.left:
                if is_leaf(node.left):
                    l.append(node.left.val)
                    node.left = None
                else:
                    dfs(l, node.left)
            if node.right:
                if is_leaf(node.right):
                    l.append(node.right.val)
                    node.right = None
                else:
                    dfs(l, node.right)

        
        if not root: return []
      
        ans, leaves = [], []    
        while root.left or root.right:
            dfs(leaves, root)
            ans.append(leaves)
            leaves = []            
        ans.append([root.val])
        
        return ans