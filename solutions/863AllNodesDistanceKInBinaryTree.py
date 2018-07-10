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
        
        adj = {}
        q = collections.deque()
        q.append(root)
        while q:
            n = q.popleft()
            if n.left:
                if n.left in adj:
                    adj[n.left].append(n)
                else:
                    adj[n.left] = [n]
                if n in adj:
                    adj[n].append(n.left)
                else:
                    adj[n] = [n.left]
                q.append(n.left)
            if n.right:
                if n.right in adj:
                    adj[n.right].append(n)
                else:
                    adj[n.right] = [n]
                if n in adj:
                    adj[n].append(n.right)
                else:
                    adj[n] = [n.right]
                q.append(n.right)
        
        ans = []
        
        nodes = set()
        q = collections.deque()
        q.append((target, 0))
        while q:
            n, d = q.popleft()
            if d > K:
                break
            if d == K and n != target:
                ans.append(n.val)
            if n in adj:
                for node in adj[n]:
                    if node not in nodes:
                        q.append((node, d+1))
                        nodes.add(node)
        
        return ans
        
            
        