# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        index = 0
        
        while n:
            buf4 = [''] * 4
            res = read4(buf4)
            if not res: 
                return index
            
            for i in range(min(res, n)):
                buf[index] = buf4[i]
                index += 1
                n -= 1
        
        return index
        