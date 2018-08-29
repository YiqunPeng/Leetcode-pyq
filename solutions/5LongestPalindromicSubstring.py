class Solution:
    # dp
    # time: O(n^2)
    # space: O(n^2)
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ''

        s_len = len(s) 
        dp = [[False] * s_len for i in range(s_len)]

        left, right = 0, 0
        for i in range(s_len):
            for j in range(i):
                if s[i] == s[j] and (i - j <= 2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if i - j > right - left:
                        left, right = j, i

        return s[left:right+1]       