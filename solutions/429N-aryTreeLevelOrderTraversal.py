"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root: return []
        
        ans = []
        queue = collections.deque([(root, 0)])
        
        while queue:
            node, lvl = queue.popleft()
            if not ans or lvl >= len(ans):
                ans.append([node.val])
            else:
                ans[lvl].append(node.val)
            for c in node.children:
                queue.append((c, lvl+1))
        
        return ans
