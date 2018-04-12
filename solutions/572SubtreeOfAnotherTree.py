class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def subtree(s, t):
            if not s and not t: return True
            if (s and not t) or (not s and t): return False
            if s.val != t.val: return False
            return subtree(s.left, t.left) and subtree(s.right, t.right)
    
        
        def traverse(root, t):
            if not root: return False
            if root.val == t.val:
                if subtree(root, t):
                    return True
            if root.left:
                if traverse(root.left, t):
                    return True
            if root.right:
                if traverse(root.right, t):
                    return True
            return False
        
        return traverse(s, t)
            
        