class Solution:
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        def reverse(ans, s, e):
            while s < e:
                ans[s], ans[e] = ans[e], ans[s]
                s, e = s + 1, e - 1 
 

        ans = [i for i in range(1, len(s)+2)]
        
        d_i = -1
        for i in range(len(s)):
            if s[i] == 'D':
                if d_i == -1:
                    d_i = i
            else:
                if d_i != -1:
                    reverse(ans, d_i, i)
                d_i = -1
        
        if d_i != -1:
            reverse(ans, d_i, len(ans)-1)
                     
        return ans
                
        