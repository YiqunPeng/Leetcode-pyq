# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = n_head = ListNode(0)
        n_head.next = head
        
        while head and head.next:
            val = head.next.val
            if head.val <= val:
                head = head.next
                continue
                
            p = n_head
            while p.next.val <= val:
                p = p.next
                
            node = head.next
            head.next = node.next
            node.next = p.next
            p.next = node
            
        return n_head.next         