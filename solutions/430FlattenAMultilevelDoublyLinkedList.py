"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    # stack
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """ 
        if not head: return None
        
        n_head = Node(0, None, None, None)
        o_head = n_head

        stack = [head]
        while stack:
            node = stack.pop()
            n_head.next = Node(node.val, n_head, None, None)
            n_head = n_head.next
            
            if node.next: stack.append(node.next)
            if node.child: stack.append(node.child)
                
        o_head.next.prev = None
        return o_head.next       
    
    
    
    # preorder traversal
    # def __init__(self):
    #     self.new_head = Node(0, None, None, None)
    #     self.old_head = self.new_head


    # def flatten(self, head):
    #     """
    #     :type head: Node
    #     :rtype: Node
    #     """          
    #     def preorder(node):
    #         if not node: return

    #         curr = Node(node.val, self.new_head, None, None)
    #         self.new_head.next = curr
    #         self.new_head = curr

    #         preorder(node.child)
    #         preorder(node.next)


    #     preorder(head)
    #     if self.old_head.next: self.old_head.next.prev = None
    #     return self.old_head.next
        
  

    # dfs
    # def __init__(self):
    #     self.new_head = Node(0, None, None, None)
    #     self.old_head = self.new_head

    # def flatten(self, head):
    #     """
    #     :type head: Node
    #     :rtype: Node
    #     """
    #     def dfs(head):
    #         while head:
    #             nxt = Node(head.val, self.new_head, None, None)                  
    #             self.new_head.next = nxt
    #             self.new_head = self.new_head.next
    #             if head.child:
    #                 self.new_head = dfs(head.child)
    #             head = head.next

    #         return self.new_head


    #     dfs(head)
    #     if self.old_head.next: self.old_head.next.prev = None
    #     return self.old_head.next        