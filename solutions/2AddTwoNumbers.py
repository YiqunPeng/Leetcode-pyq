# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        old_head = head
        
        carry = 0
        
        while l1 or l2:
            nxt = ListNode(carry)
            carry = 0
            
            if l1:
                nxt.val += l1.val
                l1 = l1.next
            if l2:
                nxt.val += l2.val
                l2 = l2.next
                
            if nxt.val >= 10:
                carry = 1
                nxt.val -= 10
                
            head.next = nxt
            head = head.next
        
        if carry == 1:
            head.next = ListNode(1)
        return old_head.next