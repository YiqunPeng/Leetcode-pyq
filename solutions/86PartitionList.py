# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head: return None

        sm, o_sm, la, o_la = None, None, None, None
        while head:
            ne = head.next
            if head != sm and head.val < x:
                if not sm:
                    sm = head
                    o_sm = head
                else:
                    sm.next = head
                    sm = sm.next
            if head != la and head.val >= x:
                if not la:
                    la = head
                    o_la = head
                else:
                    la.next = head
                    la = la.next
            head = ne
        
        if sm: sm.next = o_la
        if la: la.next = None
        
        if o_sm:
            return o_sm
        else:
            return o_la