# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        if not root: return []
        if K == 0: return [target.val]
        
        adj = collections.defaultdict(set)
        q = collections.deque([root])
        while q:
            n = q.popleft()
            if n.left:
                adj[n.left].add(n)
                adj[n].add(n.left)
                q.append(n.left)
            if n.right:
                adj[n.right].add(n)
                adj[n].add(n.right)
                q.append(n.right)
        
        ans = []   
        seen = set()
        q = collections.deque([(target, 0)])
        while q:
            n, d = q.popleft()
            if d > K: return ans
            if d == K and n != target:
                ans.append(n.val)
            for node in adj[n]:
                if node not in seen:
                    q.append((node, d+1))
                    seen.add(node)
        
        return ans