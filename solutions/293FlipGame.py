class Solution:
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        
        for i in range(1, len(s)):
            if s[i-1] == s[i] == '+':
                ans.append(s[:i-1] + '--' + s[i+1:])
    
        return ans