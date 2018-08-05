# queue
# time: O(n) n -- number of total elements
# space: O(k) k -- number of vectors
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.vectors = [v1, v2]
        self.queue = collections.deque()
        for i in range(len(self.vectors)):
            if self.vectors[i]: self.queue.append((i, 0))
        
    def next(self):
        """
        :rtype: int
        """
        vec, pos = self.queue.popleft()
        if pos + 1 < len(self.vectors[vec]): self.queue.append((vec, pos + 1))
        return self.vectors[vec][pos]              

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.queue else False
            

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())