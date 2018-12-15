# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def sort(head):
            if not head or not head.next: return head
            
            slow, fast, prev = head, head, None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            prev.next = None
  
            f_half = sort(head)
            s_half = sort(slow)
            
            return merge(f_half, s_half)
            
        
        def merge(head1, head2):
            n_head = o_head = ListNode(0)
            
            while head1 and head2:
                if head1.val <= head2.val:
                    n_head.next = head1
                    head1 = head1.next
                else:
                    n_head.next = head2
                    head2 = head2.next
                n_head = n_head.next
                
            if head1: n_head.next = head1
            if head2: n_head.next = head2
            
            return o_head.next
        
        
        return sort(head)