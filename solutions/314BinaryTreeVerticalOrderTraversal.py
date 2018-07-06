import queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def depth(node, d):
            if not node:
                return d - 1
            return max(depth(node.left, d+1), depth(node.right, d+1))
        
        if not root: return []
        
        d = depth(root, 1)
        res = [[] for i in range(d*2+1)]
        res[d] = [root.val]
        
        q = queue.Queue()
        q.put((root, d))
        while not q.empty():
            node, pos = q.get()
            if node.left:
                q.put((node.left, pos-1))
                res[pos-1].append(node.left.val)
            if node.right:
                q.put((node.right, pos+1))
                res[pos+1].append(node.right.val)

        ans = []
        for r in res:
            if r:
                ans.append(r)
        return ans
        