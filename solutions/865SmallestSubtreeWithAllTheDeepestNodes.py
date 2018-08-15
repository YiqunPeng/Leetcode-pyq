# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        
        father = {}
        
        def max_depth(n, d):
            if not n:
                return d - 1
            return max(max_depth(n.left, d+1), max_depth(n.right, d+1))            
        
        depth = max_depth(root, 1)        
        nodes = [[] for i in range(depth)]
        deepest = set()
        q = collections.deque()
        q.append((root, 1))
        while q:
            n, d = q.popleft()
            if d == depth:
                deepest.add(n)
            nodes[d-1].append(n)
            if n.left: 
                father[n.left] = n
                q.append((n.left, d+1))
            if n.right: 
                father[n.right] = n
                q.append((n.right, d+1))
        
        while len(deepest) != 1:
            temp = set()
            for d in deepest:
                temp.add(father[d])
            deepest = temp
        node = deepest.pop()
        
        return node
        
            
        
        
        
        
