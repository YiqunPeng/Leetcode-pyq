class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        def volume(height, left, right):
            return min(height[left], height[right]) * (right - left)
        
        
        max_n = len(height)
        left, right = 0, max_n - 1
        ans = volume(height, left, right)
        
        while left < right:
            old_left, old_right = height[left], height[right]
            if old_left < old_right:
                while left + 1 < max_n and height[left+1] <= old_left:
                    left += 1
                left += 1
            else:
                while right - 1 >= 0 and height[right-1] <= old_right:
                    right -= 1
                right -= 1
            vol = volume(height, left, right)
            ans = max(ans, vol)  
        
        return ans
        