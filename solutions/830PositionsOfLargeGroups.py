class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        if not S: return []
      
        ans = []

        start = 0
        for i in range(1, len(S)):
            if S[i] != S[i-1]:
                if i - start >= 3:
                    ans.append([start, i - 1])
                start = i

        if len(S) - start >= 3:
            ans.append([start, len(S) - 1])
        return ans
        
