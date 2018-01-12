class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s: return ''
        if numRows == 1: return s
        
        rows = [[] for i in range(numRows)]
        ans = ''
        
        mode, pos = 1, 0
        for c in s:
            rows[pos].append(c)
            if mode == 1:
                if pos == numRows - 1 and numRows > 2:
                    mode = 0
                    pos = numRows - 2
                elif pos == numRows - 1 and numRows == 2:
                    pos = 0            
                else:
                    pos += 1
            elif mode == 0:
                if pos == 1:
                    mode = 1
                    pos = 0
                else:
                    pos -= 1
        
        for row in rows:
            for c in row:
                ans += c
        
        return ans