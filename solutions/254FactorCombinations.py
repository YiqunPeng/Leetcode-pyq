class Solution:
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def backtracking(ans, cur, re, pre, n):
            for i in range(pre, int(math.sqrt(n))+1, 1):
                if re % i == 0:
                    if re // i != 1 and re // i >= i:
                        ans.append(cur+[i]+[re//i])
                    if re != 1:
                        backtracking(ans, cur+[i], re//i, i, n)
        
        if n == 1: return []
        
        ans = []
        backtracking(ans, [], n, 2, n)
        return ans