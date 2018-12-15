# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def plus_one(head):
            if not head.next:
                head.val += 1
            else:
                plus_one(head.next)
                if head.next.val >= 10:
                    head.next.val -= 10
                    head.val += 1
        
        
        n_head = ListNode(0)
        n_head.next = head
        
        plus_one(n_head)
        if n_head.val == 1:
            return n_head
        else:
            return n_head.next