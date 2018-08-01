"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        def depth(node, d):
            if not node: return d - 1
            if node.children:
                return max([depth(n, d+1) for n in node.children])
            else:
                return d
        
        return depth(root, 1)