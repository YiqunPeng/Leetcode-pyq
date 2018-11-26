class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        n = len(S) + 1
        
        ans = [-1] * n

        low = 0
        for i in range(len(S)-1, -1, -1):
            if S[i] == 'D':
                ans[i+1] = low
                low += 1

        high = n - 1
        for i in range(len(S)-1, -1, -1):
            if S[i] == 'I':
                ans[i+1] = high
                high -= 1                
        ans[0] = high

        return ans 