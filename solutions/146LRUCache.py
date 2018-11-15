class DoublyLinkedNode:
    
    def __init__(self, val = None, pre = None, nxt = None):
        self.val = val
        self.prev = pre
        self.next = nxt
        
        
class DoublyLinkedList:
    
    def __init__(self):
        self.head = DoublyLinkedNode()
        self.tail = DoublyLinkedNode()
        
        self.head.next = self.tail
        self.tail.prev = self.head

  
    def insert_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        
        self.head.next.prev = node
        self.head.next = node        
    
    
    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    
    def delete_tail(self):
        val = self.tail.prev.val
        
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        
        return val
        
    
    def move_node_to_head(self, node):
        self.delete_node(node)
        self.insert_head(node)
        


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.map = {}
        self.nodes = {}
        self.capacity = capacity
        
        self.linked_list = DoublyLinkedList()


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.map: return -1
        
        res = self.map[key]
        node = self.nodes[key]
        
        self.linked_list.move_node_to_head(node)
        return res
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.map:
            self.map[key] = value
            node = self.nodes[key]
            self.linked_list.move_node_to_head(node)
        
        else:
            if len(self.map) == self.capacity:
                v = self.linked_list.delete_tail()
                del self.map[v]
                del self.nodes[v]
            
            node = DoublyLinkedNode(key)
            self.linked_list.insert_head(node)
            
            self.map[key] = value
            self.nodes[key] = node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)