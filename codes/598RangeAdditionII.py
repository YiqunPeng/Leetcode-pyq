class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if len(ops) == 0:
            return m * n
        a_min = 100000
        b_min = 100000
        for op in ops:
            if op[0] < a_min:
                a_min = op[0]
            if op[1] < b_min:
                b_min = op[1]
        return a_min * b_min