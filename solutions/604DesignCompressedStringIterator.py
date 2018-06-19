class StringIterator:

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.string = compressedString
        self.char = ''
        self.cnt = 0
        self.pos = 0
        
    def next(self):
        """
        :rtype: str
        """
        if self.cnt == 0 and not self.hasNext():
            return ' '
        if self.cnt > 0:
            self.cnt -= 1
            return self.char
        else:
            self.char = self.string[self.pos]
            self.pos += 1
            while self.pos < len(self.string) and self.string[self.pos] in string.digits:
                self.cnt = self.cnt * 10 + int(self.string[self.pos])
                self.pos += 1
            self.cnt -= 1
            return self.char
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.pos != len(self.string) or self.cnt != 0


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()