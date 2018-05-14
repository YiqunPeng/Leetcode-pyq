class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        q = [0]
        ans = 0
        v = [False] * (n + 1)
        
        while q:
            ans += 1
            temp = []
            for i in q:
                j = 1
                t = i + j * j
                while t <= n:
                    if not v[t]:
                        if t < n:
                            temp.append(t)
                            v[t] = True
                        else:
                            return ans
                    j += 1
                    t = i + j * j
            q = temp
        
        return ans
        
                    
                
     
        
        