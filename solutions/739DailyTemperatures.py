class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        t = temperatures
        n = len(t)
        
        ans = [0] * n
        
        stack = [0]
        for i in range(1, n):
            if t[stack[-1]] >= t[i]:
                stack.append(i)
            else:
                while stack and t[stack[-1]] < t[i]:
                    idx = stack.pop()
                    ans[idx] = i - idx
                stack.append(i)
        
        return ans    