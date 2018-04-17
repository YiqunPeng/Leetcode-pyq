# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        odd = head
        o_odd = odd
        if not head.next: return head
        even = head.next
        o_even = even
        
        odd_flag = True
        head = head.next.next
        
        while head:
            if odd_flag:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next
            odd_flag = not odd_flag
        
        odd.next = o_even
        even.next = None
        return o_odd
        
        
        