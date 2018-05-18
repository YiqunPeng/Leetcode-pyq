# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head: return
        
        one, two = head, head
        while two and two.next and two.next.next:
            one = one.next
            two = two.next.next
        
        r_head = one.next
        tail = None
        pre = None
        while r_head:
            if not r_head.next:
                tail = r_head
            curr = r_head
            r_head = r_head.next
            curr.next = pre
            pre = curr
        
        o_head = head
        one.next = None
        
        while o_head:
            n_head = o_head.next
            o_head.next = tail
            if tail and tail.next:
                tail = tail.next
            else:
                tail = None
            if o_head.next:
                o_head.next.next = n_head
            o_head = n_head
        
        
            
    
        