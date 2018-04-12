# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = ListNode(0)
        head = l
        while l1 or l2:
            if l1:
                l.val += l1.val
                l1 = l1.next
            if l2:
                l.val += l2.val
                l2 = l2.next
            if l1 or l2:
                l.next = ListNode(l.val / 10)
                l.val = l.val % 10
                l = l.next
        if l.val >= 10:
            l.val -= 10
            l.next = ListNode(1)
        return head