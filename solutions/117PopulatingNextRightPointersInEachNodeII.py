# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        def find_next(parent, child):
            parent = parent.next
            while parent:
                if parent.left:
                    child.next = parent.left
                    return
                elif parent.right:
                    child.next = parent.right
                    return 
                else:
                    parent = parent.next
        
                        
        if not root: return
        q = [root]
        while q:
            nxt = []
            for node in q:
                if node.left:
                    if node.right:
                        node.left.next = node.right
                    else:
                        find_next(node, node.left)
                    nxt.append(node.left)
                if node.right: 
                    find_next(node, node.right)
                    nxt.append(node.right)
            q = nxt