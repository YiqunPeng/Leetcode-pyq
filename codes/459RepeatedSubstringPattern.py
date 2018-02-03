class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def discompose(num):
            res = []
            for i in range(1, num//2+1):
                if num % i == 0:
                    res.append(i)
            return res
        
        
        def match(s, p, s_len, p_len):
            pos = 0
            for i in range(p_len, s_len):
                if p[pos] == s[i]:
                    pos += 1
                    if pos == p_len:
                        pos = 0
                else:
                    return False
            return True
        
        
        s_len = len(s)
        factors = discompose(s_len)
        for f in factors:
            if s_len % 2 == 1 and f % 2 == 0: continue
            pattern = s[0:f]
            if match(s, pattern, s_len, f):
                return True
            
        return False