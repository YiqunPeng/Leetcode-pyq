class Solution:
    # string
    # time: O(n * m) m -- sequence length
    # space: O(m)
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        if n <= 1: return s
        
        for i in range(1, n):
            next_s = ''
            cnt = 1
            c = s[0]
            for j in range(1, len(s)):
                if s[j] == c:
                    cnt += 1
                else:
                    next_s = next_s + str(cnt) + c
                    cnt = 1
                    c = s[j]
            s = next_s + str(cnt) + c
        
        return s