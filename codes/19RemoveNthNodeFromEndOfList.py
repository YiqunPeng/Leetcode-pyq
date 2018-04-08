# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        left, right = head, head
        for i in range(n-1):
            right = right.next
        
        if right.next:
            right = right.next
        else:
            return head.next
        
        while right.next:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return head