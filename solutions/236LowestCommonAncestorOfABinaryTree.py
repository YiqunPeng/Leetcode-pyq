# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_d, q_d = -1, -1
        
        father = {}
        queue = collections.deque([(root, 0)])
        while queue:
            n, d = queue.popleft()
            if n == p: p_d = d
            if n == q: q_d = d
            if n.left:
                father[n.left] = n
                queue.append((n.left, d+1))
            if n.right:
                father[n.right] = n
                queue.append((n.right, d+1))

        if p_d < q_d: 
            p, q = q, p
            p_d, q_d = q_d, p_d
        while p_d != q_d:
            if p != root:
                p = father[p]
                p_d -= 1
        
        while p != q:
            p = father[p]
            q = father[q]
        
        return q