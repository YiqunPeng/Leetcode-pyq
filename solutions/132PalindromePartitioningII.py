class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        
        n = len(s)
        is_palind = [[False] * n for i in range(n)]
        min_cuts = [i for i in range(n)]

        for i in range(n):
            is_palind[i][i] = True
            for j in range(i + 1):
                if s[i] == s[j] and (j + 1 >= i - 1 or is_palind[j+1][i-1]):
                    is_palind[j][i] = True
                    min_cuts[i] = min(min_cuts[i], min_cuts[j-1] + 1) if j else 0

        return min_cuts[-1]          