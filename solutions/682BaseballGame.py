class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        ans = 0
        valid_rounds = []
        
        for op in ops:
            if op == 'C':
                ans -= valid_rounds.pop(-1)
            elif op == 'D':
                point = 2 * valid_rounds[-1]
                ans += point
                valid_rounds.append(point)
            elif op == '+':
                point = valid_rounds[-1] + valid_rounds[-2]
                ans += point
                valid_rounds.append(point)
            else:
                point = int(op)
                ans += point
                valid_rounds.append(point)
        
        return ans