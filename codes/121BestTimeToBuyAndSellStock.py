class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        
        ans = 0
        min_price = prices[0]
        
        for p in prices:
            min_price = min(min_price, p)
            ans = max(ans, p - min_price)
        
        return ans