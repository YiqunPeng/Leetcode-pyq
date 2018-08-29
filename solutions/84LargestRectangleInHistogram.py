class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights: return 0
        heights.append(0)
        
        n = len(heights)
        ans = 0
        
        stack = [-1]
        for i in range(n):
            while heights[stack[-1]] > heights[i]:
                pos = stack.pop()
                ans = max(ans, (i - stack[-1] - 1) * heights[pos])
            stack.append(i)
        
        heights.pop()
        return ans