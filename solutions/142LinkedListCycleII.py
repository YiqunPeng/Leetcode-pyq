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
        if not head: return None
   
        fast, slow = head, head
    
        has_cycle = False
        
        while fast and slow:
            if not fast.next or not fast.next.next:
                return None
            fast = fast.next.next 
            if not slow.next:
                return None
            slow = slow.next
            if fast == slow:
                has_cycle = True
                break
        
        if not has_cycle: return None
        
        start = head
        while start != slow:
            start = start.next
            slow = slow.next
        
        return slow
            
        