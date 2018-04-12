# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        
        self.delete(head)
        
        return head
    
    def delete(self, head):
        if head == None or head.next == None:
            return
        else:
            while head.next and head.val == head.next.val:
                head.next = head.next.next
            self.delete(head.next)