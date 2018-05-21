class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = []
        for i in range(len(vec2d)):
            for j in range(len(vec2d[i])):
                self.vec2d.append(vec2d[i][j])
        self.pos = 0
        

    def next(self):
        """
        :rtype: int
        """   
        val = self.vec2d[self.pos]
        self.pos += 1
        return val
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.pos < len(self.vec2d):
            return True
        else:
            return False

        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())