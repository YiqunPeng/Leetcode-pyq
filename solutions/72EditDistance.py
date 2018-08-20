class Solution:
    # dp
    # time: O(n * m) n -- length of word1, m -- length of word2
    # space: O(n)
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [i for i in range(len(word1) + 1)]
        
        for j in range(1, len(word2) + 1):
            pre = dp[0]
            dp[0] = j
            for i in range(1, len(word1) + 1):
                temp = dp[i]
                if word1[i-1] == word2[j-1]:
                    dp[i] = pre
                else:
                    dp[i] = min(pre, dp[i], dp[i-1]) + 1
                pre = temp
        
        return dp[-1]
        
            
    # dp
    # time: O(n * m)
    # space: O(n)
    # def minDistance(self, word1, word2):
    #     """
    #     :type word1: str
    #     :type word2: str
    #     :rtype: int
    #     """
    #     if not word1 and not word2: return 0
    #     if not word1: return len(word2)
    #     if not word2: return len(word1)

    #     dp = [[0] * (len(word1) + 1) for i in range(2)]
    #     for i in range(len(word1) + 1):
    #         dp[0][i] = i

    #     for j in range(1, len(word2) + 1):
    #         dp[j%2][0] = j
    #         for i in range(1, len(word1) + 1):
    #             if word1[i-1] == word2[j-1]:
    #                 dp[j%2][i] = dp[1-j%2][i-1]
    #             else:
    #                 dp[j%2][i] = min(dp[1-j%2][i-1], dp[j%2][i-1], dp[1-j%2][i]) + 1

    #     return dp[len(word2)%2][-1]

    
    # dp
    # time: O(n * m) 
    # space: O(n * m)
    # def minDistance(self, word1, word2):
    #     """
    #     :type word1: str
    #     :type word2: str
    #     :rtype: int
    #     """
    #     if not word1 and not word2: return 0
    #     if not word1: return len(word2)
    #     if not word2: return len(word1)

    #     dp = [[0 for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]
    #     for j in range(1, len(word2) + 1):
    #         dp[0][j] = j
    #     for i in range(1, len(word1) + 1):
    #         dp[i][0] = i

    #     for i in range(1, len(word1) + 1):
    #         for j in range(1, len(word2) + 1):
    #             if word1[i-1] == word2[j-1]:
    #                 dp[i][j] = dp[i-1][j-1]
    #             else:
    #                 dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1

    #     return dp[-1][-1]