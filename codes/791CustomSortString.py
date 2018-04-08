class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        s_table = [0] * 26
        t_table = [0] * 26
        
        for s in S:
            s_table[ord(s)-ord('a')] = 1
        
        ans = ''
        
        for t in T:
            t_table[ord(t)-ord('a')] += 1
        
        for s in S:
            ans = ans + s * t_table[ord(s)-ord('a')]
            t_table[ord(s)-ord('a')] = 0
                    
        for i in range(len(t_table)):
            ans = ans + t_table[i] * chr(ord('a') + i)
                                    
        return ans