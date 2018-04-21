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
        old_head = head
        while head:
            if not head.next:
                head.val += 1
            head = head.next
        
        flag = False
        while not flag:
            flag = True
            head = old_head
            if head.val > 9:
                new_head = ListNode(0)
                new_head.next = old_head
                old_head = new_head
                head = old_head
            while head.next:
                if head.next.val > 9:
                    head.val += 1
                    head.next.val -= 10
                    flag = False
                head = head.next

        return old_head
    