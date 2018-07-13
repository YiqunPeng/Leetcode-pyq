# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head: return None
        
        dic = {None: None}
        old_head = head
        
        c_head = RandomListNode(head.label)
        dic[head] = c_head
        
        while head.next:
            head = head.next
            c_next = RandomListNode(head.label)
            c_head.next = c_next
            c_head = c_next
            dic[head] = c_head
        
        head = old_head
        c_head = dic[head]
        c_head.random = dic[head.random] 
        while head.next:
            head = head.next
            c_head = c_head.next
            c_head.random = dic[head.random]
        
        return dic[old_head]