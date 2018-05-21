class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1 = v1
        self.v2 = v2
        self.vectors = [self.v1, self.v2]
        self.num_vec = len(self.vectors)
        self.curr_vec = 0
        self.pos = [0, 0]
        self.length = [len(self.v1), len(self.v2)]
        

    def next(self):
        """
        :rtype: int
        """
        val = 0
        if self.pos[self.curr_vec] < self.length[self.curr_vec]:
            val = self.vectors[self.curr_vec][self.pos[self.curr_vec]]
            self.pos[self.curr_vec] += 1
            self.curr_vec = (self.curr_vec + 1) % self.num_vec
        else:
            for i in range(self.num_vec-1):
                curr = (self.curr_vec + 1 + i) % self.num_vec
                if self.pos[curr] < self.length[curr]:
                    val = self.vectors[curr][self.pos[curr]]
                    self.pos[curr] += 1
                    self.curr_vec = (curr + 1) % self.num_vec
        return val                  
            

    def hasNext(self):
        """
        :rtype: bool
        """
        res = False
        for i in range(self.num_vec):
            if self.pos[i] < self.length[i]:
                return True
        return False
            

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())