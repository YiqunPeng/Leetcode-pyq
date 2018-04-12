# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        v = root.val
        v_p, v_q = p.val, q.val
        if v == v_p or v == v_q:
            return root
        if (v>v_p and v<v_q) or (v>v_q and v<v_p):
            return root
        if v > max(v_p, v_q):
            return self.lowestCommonAncestor(root.left, p, q)
        elif v < min(v_p, v_q):
            return self.lowestCommonAncestor(root.right, p, q)
            