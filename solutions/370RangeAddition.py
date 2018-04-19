class Solution:
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        ans = [0] * length
        
        for s, e, v in updates:
            ans[s] += v
            if e < length - 1:
                ans[e+1] -= v
        
        sum = 0
        for i in range(length):
            sum += ans[i]
            ans[i] = sum
        
        return ans