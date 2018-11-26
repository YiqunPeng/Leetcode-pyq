class Solution:
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        if not tokens: return 0
        
        tokens.sort()
        ans = 0
        
        points = 0
        
        if tokens[0] > P: return 0
        
        while tokens and P - tokens[0] >= 0:
            points += 1
            P = P - tokens.pop(0)
        ans = points

        if not tokens: return ans
        
        P = P + tokens.pop()
        points -= 1
        
        while tokens and points >= 0:
            while tokens and P - tokens[0] >= 0:
                points += 1
                P = P - tokens.pop(0)
            ans = max(ans, points)
            
            if not tokens: break
            
            points -= 1
            P = P + tokens.pop()
            
        return ans