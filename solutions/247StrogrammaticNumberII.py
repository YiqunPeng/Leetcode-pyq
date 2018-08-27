class Solution:
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(length, remain):
            if remain == 0: return ['']
            if remain == 1: return ['0', '1', '8']

            sub_res = dfs(length, remain - 2)

            res = []
            for num in sub_res:
                if length != remain: res.append('0' + num + '0')
                res.append('1' + num + '1')
                res.append('6' + num + '9')
                res.append('8' + num + '8')
                res.append('9' + num + '6')

            return res
        
        return dfs(n, n)
