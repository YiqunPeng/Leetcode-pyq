class Solution:
    # dp
    # time: O(n^2)
    # space: O(n)
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle or not triangle[0]: return 0
        
        n = len(triangle)
        
        dp = [sys.maxsize] * n
        dp[0] = triangle[0][0]
        
        for i in range(1, n):
            pre = dp[0]
            
            for j in range(i + 1):
                pre_j = dp[j]
                
                if j == 0:
                    dp[j] = pre_j + triangle[i][j]
                elif j == i:
                    dp[j] = pre + triangle[i][j]
                else:
                    dp[j] = min(pre, pre_j) + triangle[i][j]
        
                pre = pre_j
        
        return min(dp)
   

    # dp
    # time: O(n^2)
    # space: O(n)
    # def minimumTotal(self, triangle):
    #     """
    #     :type triangle: List[List[int]]
    #     :rtype: int
    #     """
    #     if not triangle or not triangle[0]: return 0

    #     n = len(triangle)

    #     dp = [[sys.maxsize] * n for i in range(2)]
    #     dp[0][0] = triangle[0][0]

    #     for i in range(1, n):
    #         for j in range(i + 1):
    #             if j == 0:
    #                 dp[i%2][j] = dp[1-i%2][0] + triangle[i][j]
    #             elif j == i:
    #                 dp[i%2][j] = dp[1-i%2][j-1] + triangle[i][j]
    #             else:
    #                 dp[i%2][j] = min(dp[1-i%2][j-1], dp[1-i%2][j]) + triangle[i][j]

    #     return min(dp[1-n%2])
    
    
    # dp
    # time: O(n * n) n -- numbers of rows
    # space: O(n * n)
    # def minimumTotal(self, triangle):
    #     """
    #     :type triangle: List[List[int]]
    #     :rtype: int
    #     """
    #     if not triangle or not triangle[0]: return 0

    #     n = len(triangle)

    #     dp = [[sys.maxsize] * n for i in range(n)]
    #     dp[0][0] = triangle[0][0]

    #     for i in range(1, n):
    #         for j in range(i + 1):
    #             if j == 0:
    #                 dp[i][j] = dp[i-1][0] + triangle[i][j]
    #             elif j == i:
    #                 dp[i][j] = dp[i-1][j-1] + triangle[i][j]
    #             else:
    #                 dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

    #     return min(dp[-1])