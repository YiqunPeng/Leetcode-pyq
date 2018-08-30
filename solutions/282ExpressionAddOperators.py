class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        def dfs(curr, re, c_sum, last, res):
            if not re:
                if c_sum == target:
                    res.append(curr)
                return
            
            for i in range(len(re)):
                if i == 0 or (i > 0 and re[0] != '0'):
                    dfs(curr+'+'+re[:i+1], re[i+1:], c_sum+int(re[0:i+1]), int(re[0:i+1]), res)
                    dfs(curr+'-'+re[:i+1], re[i+1:], c_sum-int(re[0:i+1]), -int(re[0:i+1]), res)
                    dfs(curr+'*'+re[:i+1], re[i+1:], (c_sum-last)+last*int(re[0:i+1]), last*int(re[0:i+1]), res)
        
        
        ans = []
        
        for i in range(len(num)):
            if i == 0 or (i > 0 and num[0] != '0'):
                dfs(num[:i+1], num[i+1:], int(num[:i+1]), int(num[:i+1]), ans)
        
        return ans