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
        dummy = ListNode(-1)
        dummy.next = head
        o_head = dummy
        
        while dummy.next:
            if dummy.next.next and dummy.next.val == dummy.next.next.val:
                while dummy.next.next and dummy.next.val == dummy.next.next.val:
                    dummy.next = dummy.next.next
                dummy.next = dummy.next.next     
            else:
                if dummy.next: dummy = dummy.next
        
        return o_head.next