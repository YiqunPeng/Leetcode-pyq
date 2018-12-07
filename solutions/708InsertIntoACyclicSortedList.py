"""
# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution:
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        if not head:
            head = Node(insertVal, None)
            head.next = head
            return head
        
        o_head = head
        
        smallest, greatest = None, head
        head = head.next
        while head is not o_head:
            if greatest.val < head.val and head.next.val != head.val:
                greatest = head
            head = head.next
        smallest = greatest.next

        if insertVal <= smallest.val or insertVal >= greatest.val:
            greatest.next = Node(insertVal, smallest)
            return o_head

        head = smallest
        while head.next is not smallest:
            if head.val <= insertVal <= head.next.val:
                head.next = Node(insertVal, head.next)
                return o_head
            head = head.next