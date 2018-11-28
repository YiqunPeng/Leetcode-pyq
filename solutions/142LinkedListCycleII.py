# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        has_cycle = False
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow is fast: 
                has_cycle = True
                break
                
        if not has_cycle: return None
        
        start = head
        while start is not slow:
            start = start.next
            slow = slow.next
            
        return start    