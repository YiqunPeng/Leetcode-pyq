class LinkedListNode:
    
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = LinkedListNode()
        
    
    def print_list(self):
        nhead = self.head
        res = []
        while nhead:
            res.append(nhead.val)
            nhead = nhead.next
        print(res)
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0: return -1
        
        head = self.head
        while index != 0 and head.next:
            head = head.next
            index -= 1
            
        if not head.next: return -1
            
        # self.print_list()
            
        return head.next.val
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        head = self.head
        nhead = LinkedListNode(val)
        nhead.next = head.next
        head.next = nhead 
        
        # self.print_list()
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        head = self.head
        while head.next:
            head = head.next
        ntail = LinkedListNode(val)
        head.next = ntail
        
        # self.print_list()
                

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index < 0: return

        head = self.head
        while index != 0 and head.next:
            head = head.next
            index -= 1
        
        if not head and index > 0: return
        
        ntail = LinkedListNode(val)
        if not head and index == 0: 
            head.next = ntail
        
        if head and index == 0:
            ntail.next = head.next
            head.next = ntail
            
        # self.print_list()
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index < 0: return

        head = self.head
        while index != 0 and head.next:
            head = head.next
            index -= 1
        
        if not head.next: return   
        head.next = head.next.next     
        
        # self.print_list()


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)