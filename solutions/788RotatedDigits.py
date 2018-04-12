class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        def rotate(s, dic):
            res = ''
            for c in s:
                if c in dic:
                    res = res + dic[c]
                else:
                    return "-1"
                    
            return res
            
        
        dic = {'0':'0', '1':'1', '2':'5', '5':'2', '6':'9', '8':'8', '9':'6'}
        
        ans = 0
        for i in range(1, N+1):
            i_str = str(i)
            i_r = rotate(i_str, dic)
            if i_r == "-1" or i_r == i_str: continue
            ans += 1
        
        return ans