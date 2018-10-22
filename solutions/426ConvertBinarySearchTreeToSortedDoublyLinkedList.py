"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    
    def __init__(self):
        self.dummy = Node(0, None, None)
        self.prev = self.dummy
        
    
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return None
        
        self.treeToDoublyList(root.left)
        
        root.left = self.prev
        self.prev.right = root
        self.prev = root
        
        self.treeToDoublyList(root.right)
        
        self.prev.right = self.dummy.right
        self.dummy.right.left = self.prev
        return self.prev.right