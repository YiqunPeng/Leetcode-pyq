class Solution:
    # dp
    # time: O(n * m) n -- length of S; m -- length of T
    # space: O(n)
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """    
        s_len, t_len = len(S), len(T)
        
        dp = [-1] * s_len
        for j in range(s_len):
            if S[j] == T[0]:
                dp[j] = j
            else:
                if j > 0: dp[j] = dp[j-1]
        
        for i in range(1, t_len):
            pre = dp[i-1]
            
            for j in range(i):
                dp[j] = -1
            
            for j in range(i, s_len):
                temp = dp[j]
                
                if T[i] == S[j]:
                    dp[j] = pre
                else:
                    dp[j] = dp[j-1]
                
                pre = temp
        
        pos, min_len = -1, s_len
        for j in range(s_len):
            if dp[j] != -1 and j - dp[j] + 1 < min_len:
                min_len = j - dp[j] + 1
                pos = dp[j]

        return "" if pos == -1 else S[pos:pos+min_len]
          
    
    # dp
    # time: O(n * m) 
    # space: O(n * m)
    # def minWindow(self, S, T):
    #     """
    #     :type S: str
    #     :type T: str
    #     :rtype: str
    #     """
    # s_len, t_len = len(S), len(T)

    # dp = [[-1] * s_len for i in range(t_len)]

    # for j in range(s_len):
    #     if S[j] == T[0]:
    #         dp[0][j] = j
    #     else:
    #         if j > 0:
    #             dp[0][j] = dp[0][j-1]

    # for i in range(1, t_len):
    #     for j in range(i, s_len):
    #         if T[i] == S[j]:
    #             dp[i][j] = dp[i-1][j-1]
    #         else:
    #             dp[i][j] = dp[i][j-1]

    # pos, min_len = -1, s_len
    # for j in range(s_len):
    #     if dp[-1][j] != -1 and j - dp[-1][j] + 1 < min_len:
    #         min_len = j - dp[-1][j] + 1
    #         pos = dp[-1][j]
    # print(dp)
    # return "" if pos == -1 else S[pos:pos+min_len]