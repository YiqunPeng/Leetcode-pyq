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
        def get_length(head):
            cnt = 1
            while head.next:
                head = head.next
                cnt += 1
            return cnt
        
        len1, len2 = get_length(l1), get_length(l2)
        if len1 < len2:
            node = ListNode(l2.val)
            node.next = l2.next
            l2 = l1
            l1 = node
            len1 = len1 + len2
            len2 = len1 - len2
            len1 = len1 - len2
        head = l1
        for i in xrange(len1-len2):
            l1 = l1.next
        for i in xrange(len2):
            l1.val += l2.val
            l1 = l1.next
            l2 = l2.next
        for i in xrange(len1-1, 0, -1):
            temp = head
            for j in xrange(i):
                temp = temp.next
            if temp.val >= 10:
                temp.val -= 10
                temp = head
                for j in xrange(i-1):
                    temp = temp.next
                temp.val += 1
        if head.val >= 10:
            head.val -= 10
            new_head = ListNode(1)
            new_head.next = head
            return new_head
        else:
            return head
        