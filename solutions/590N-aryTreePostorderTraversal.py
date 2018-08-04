"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root: return []
        
        dq = collections.deque()
        stack = [root]
        
        while stack:
            node = stack.pop()
            dq.appendleft(node.val)
            for c in node.children:
                stack.append(c)
        
        ans = []
        while dq:
            ans.append(dq.popleft())
        return ans
            
