# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # iteratively
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        
        while head:
            curr = head
            head = head.next
            curr.next = pre
            pre = curr
        
        return pre

    # recursively
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def recursion(node, pre):
            if not node:
                return pre
            cur = node.next
            node.next = pre
            return recursion(cur, node)
        
        return recursion(head, None)
    