class Solution:
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        res = [1]
        
        while len(res) <= N:
            res = [i * 2 - 1 for i in res] + [i * 2 for i in res]
        
        return [i for i in res if 1 <= i <= N]