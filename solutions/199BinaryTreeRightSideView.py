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
        def max_depth(node, d):
            if not node: return d - 1
            if not node.left and not node.right: return d
            return max(max_depth(node.left, d+1), max_depth(node.right, d+1))
        
        
        def dfs(ans, node, pos):
            if node.right:
                if ans[pos] == sys.maxsize:
                    ans[pos] = node.right.val
                dfs(ans, node.right, pos+1)
            if node.left:
                if ans[pos] == sys.maxsize:
                    ans[pos] = node.left.val
                dfs(ans, node.left, pos+1)
            
            
        if not root: return []
        
        depth = max_depth(root, 1)
        ans = [sys.maxsize] * depth
        ans[0] = root.val
        
        dfs(ans, root, 1)
        return ans
        