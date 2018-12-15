# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse(begin, end):
            curr = begin.next
            o_curr = curr
            prev = begin
            
            while curr != end:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            begin.next = prev
            o_curr.next = end
            return o_curr
        
        
        if not head or not head.next or k == 1: return head
        
        n_head = ListNode(0)
        n_head.next = head  
        begin = n_head
        
        idx = 0
        
        while head:
            idx += 1
            if idx % k == 0:
                begin = reverse(begin, head.next)
                head = begin.next
            else:
                head = head.next
        
        return n_head.next