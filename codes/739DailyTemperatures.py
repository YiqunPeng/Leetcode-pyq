class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        unsolved = [0]
        days = len(temperatures)
        ans = [0] * days

        for i in range(1, days):
            while len(unsolved) != 0:
                if temperatures[unsolved[-1]] < temperatures[i]:
                    ans[unsolved[-1]] = i - unsolved[-1]
                    unsolved.pop(-1)
                else:
                    break
            unsolved.append(i)                
                
        return ans