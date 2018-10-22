# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # add parent-child relationship
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """    
        
        parent = {}
        pp, pq = False, False
        
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            
            if node == p: pp = True
            if node == q: pq = True
            if pp and pq: break
                
            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            if node.right:
                parent[node.right] = node
                queue.append(node.right)
        
        ancestors = set([p])
        while p != root:
            p = parent[p]
            ancestors.add(p)
        
        while q != root:
            if q in ancestors:
                return q
            q = parent[q]
        
        return root
        
    
    # dfs
    # def lowestCommonAncestor(self, root, p, q):
    #     """
    #     :type root: TreeNode
    #     :type p: TreeNode
    #     :type q: TreeNode
    #     :rtype: TreeNode
    #     """
    #     if not root or root == p or root == q:
    #         return root

    #     left = self.lowestCommonAncestor(root.left, p, q)
    #     right = self.lowestCommonAncestor(root.right, p, q)

    #     if left and right: return root
    #     return left if left else right