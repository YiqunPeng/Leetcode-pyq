# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.queue = collections.deque()
    
    
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx = 0
        
        while self.queue and n:
            buf[idx] = self.queue.popleft()
            idx += 1
            n -= 1
            
        while n:
            buf4 = [''] * 4
            res = read4(buf4)
            
            if res == 0: return idx
            
            if res > n: self.queue.extend(buf4[n:res])
            
            for i in range(min(res, n)):
                buf[idx] = buf4[i]
                idx += 1
                n -= 1
            
        return idx