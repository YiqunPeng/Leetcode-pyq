class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        mod = 10 ** 9 + 7        
        n = len(s)
   
        dp = [0] * 3
        dp[0] = 1
        
        if s[0] == '0':
            return 0
        elif s[0] == '*':
            dp[1] = 9
        else:
            dp[1] = 1
            
        for i in range(2, n+1):
            if s[i-1] == '0':
                dp[i%3] = 0
                if s[i-2] == '0': 
                    return 0
                elif s[i-2] == '*':
                    dp[i%3] += dp[(i-2)%3] * 2
                elif s[i-2] == '1' or s[i-2] == '2':
                    dp[i%3] += dp[(i-2)%3]
            elif s[i-1] == '*':
                dp[i%3] = dp[(i-1)%3] * 9
                if s[i-2] == '*':
                    dp[i%3] += dp[(i-2)%3] * 15
                elif s[i-2] == '1':
                    dp[i%3] += dp[(i-2)%3] * 9
                elif s[i-2] == '2':
                    dp[i%3] += dp[(i-2)%3] * 6
            else:
                dp[i%3] = dp[(i-1)%3]
                if int(s[i-1]) <= 6:
                    if s[i-2] == '*':
                        dp[i%3] += dp[(i-2)%3] * 2
                    elif s[i-2] == '1' or s[i-2] == '2':
                        dp[i%3] += dp[(i-2)%3]
                else:
                    if s[i-2] == '*':
                        dp[i%3] += dp[(i-2)%3]
                    elif s[i-2] == '1':
                        dp[i%3] += dp[(i-2)%3]
            if dp[i%3] == 0: return 0

        return dp[n%3] % mod
