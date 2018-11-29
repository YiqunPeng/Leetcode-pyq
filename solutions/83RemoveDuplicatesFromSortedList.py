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
        if not head: return None
        
        o_head = head
        
        while head.next:
            if head.next.val == head.val:
                head.next = head.next.next
            else:
                if head.next: head = head.next
                
        return o_head