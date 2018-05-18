# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        pre, curr = head, head.next
        
        while curr and curr.next:
            n_curr = curr.next
            if curr.val == pre.val and curr.val == n_curr.val:
                pre.next = n_curr
            else:
                pre = pre.next
            curr = n_curr
            
        n_head = None
        while head and head.next and head.val == head.next.val:
            head = head.next.next
            
        n_head = head
        t_head = n_head
        
        while t_head and t_head.next and t_head.next.next:
            if t_head.next.val == t_head.next.next.val:
                t_head.next = t_head.next.next.next
            else:
                t_head = t_head.next
             
        return n_head
            
                