# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        pre_node = None
        while slow:
            next_node = slow.next
            slow.next = pre_node
            pre_node = slow
            slow = next_node
        
        while head and pre_node:
            if head.val != pre_node.val:
                return False
            head = head.next
            pre_node = pre_node.next
        
        return True
        
            