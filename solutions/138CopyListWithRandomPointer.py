# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    # 3 iteration
    # time: O(n)
    # space: O(1)
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head: return None
        
        old_head = head
        while head:
            nxt = head.next
            copy = RandomListNode(head.label)
            head.next = copy
            copy.next = nxt
            head = nxt
        
        head = old_head
        while head:
            if head.random:
                head.next.random = head.random.next
            head = head.next.next
        
        head = old_head
        n_head = head.next
        iter_head = n_head
        while head:
            nxt = head.next.next
            
            if nxt:
                iter_head.next = nxt.next
                iter_head = nxt.next
            else:
                iter_head.next = None
            
            head.next = nxt
            head = nxt
        
        return n_head
        
    
    # hash table
    # time: O(n)
    # space: O(n)
    # def copyRandomList(self, head):
    #     """
    #     :type head: RandomListNode
    #     :rtype: RandomListNode
    #     """
    #     if not head: return None

    #     dic = {None: None}
    #     old_head = head

    #     c_head = RandomListNode(head.label)
    #     dic[head] = c_head

    #     while head.next:
    #         head = head.next
    #         c_next = RandomListNode(head.label)
    #         c_head.next = c_next
    #         c_head = c_next
    #         dic[head] = c_head

    #     head = old_head
    #     c_head = dic[head]
    #     c_head.random = dic[head.random] 
    #     while head.next:
    #         head = head.next
    #         c_head = c_head.next
    #         c_head.random = dic[head.random]

    #     return dic[old_head]