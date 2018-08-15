# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        f, s = head, head
        
        while f.next and f.next.next:
            s = s.next
            f = f.next.next
        
        if f.next:
            return s.next
        else:
            return s