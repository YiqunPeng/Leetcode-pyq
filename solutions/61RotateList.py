# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return []
        
        old_head = head

        n = 1
        while head.next:
            n += 1
            head = head.next
        k = k % n
        head = old_head
        
        if k == 0: return head
                
        ptr1, ptr2 = head, head
        rear = head
        for i in range(k):
            ptr2 = ptr2.next
        while ptr2:
            if not ptr2.next:
                rear = ptr1
            ptr1 = ptr1.next
            ptr2 = ptr2.next
                    
        new_head = ptr1
        while ptr1.next:
            ptr1 = ptr1.next
        ptr1.next = head
        rear.next = None
        
        return new_head
                
        
                
        