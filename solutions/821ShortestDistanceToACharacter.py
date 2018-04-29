class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        c = []
        ans = []
        for i in range(len(S)):
            if S[i] == C:
                c.append(i)
                
        for i in range(c[0]):
            ans.append(c[0]-i)
                
        for i in range(len(c)-1):
            for j in range(c[i], c[i+1]):
                if S[j] == C:
                    ans.append(0)
                else:
                    ans.append(min(j-c[i], c[i+1]-j))
                    
        for i in range(c[-1], len(S)):
            ans.append(i-c[-1])
        
        return ans
                