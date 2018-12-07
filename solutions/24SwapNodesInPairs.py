# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        n_head = head.next
        
        prev = ListNode(0)
        prev.next = head
        while head and head.next:
            adja = head.next
            prev.next = adja
            
            head.next = adja.next
            adja.next = head
            prev = head
            head = head.next
            
        return n_head      