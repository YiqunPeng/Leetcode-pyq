class Solution:
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
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
        
        
        min_d, max_d = len(low), len(high)
        if min_d > max_d: return 0
        
        ans = 0
        for i in range(min_d + 1, max_d):
            if i % 2 == 0:
                ans += 4 * (5 ** (i // 2 - 1))
            else:
                if i != 1:
                    ans += 4 * (5 ** (i // 2 - 1)) * 3
                else:
                    ans += 3

        res = dfs(min_d, min_d)
        for num in res:
            if low <= num: 
                if (min_d == max_d and num <= high) or min_d != max_d:
                    ans += 1

        res = dfs(max_d, max_d) if max_d != min_d else []
        for num in res:
            if num <= high: ans += 1

        return ans
