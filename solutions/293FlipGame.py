class Solution:
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        
        for i in range(len(s)-1):
            if s[i] == '+' and s[i+1] == '+':
                temp = s[0:i] + '--' + s[i+2:]
                ans.append(temp)
        
        return ans
        