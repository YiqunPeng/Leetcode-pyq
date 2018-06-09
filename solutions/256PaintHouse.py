class Solution:
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs: return 0
        
        house_num = len(costs)
        color_num = 3
        
        dp = [[0 for j in range(color_num)] for i in range(2)]
        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]
        
        for i in range(1, house_num):
            dp[i%2][0] = min(dp[1-i%2][1], dp[1-i%2][2]) + costs[i][0]
            dp[i%2][1] = min(dp[1-i%2][0], dp[1-i%2][2]) + costs[i][1]
            dp[i%2][2] = min(dp[1-i%2][0], dp[1-i%2][1]) + costs[i][2]
        
        return min(dp[1-house_num%2])
        
