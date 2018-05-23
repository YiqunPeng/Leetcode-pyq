class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        stack = []
        length = len(height)
        
        right = 0
        while right < length:
            if height[right] == 0:
                right += 1
                continue
            if not stack:
                stack.append(right)
                right += 1
                continue

            left = stack[-1]
            if height[right] <= height[left]:
                for i in range(left+1, right):
                    ans += max(height[right] - height[i], 0)
                    height[i] = height[right]
                stack.append(right)
            else:
                while len(stack) > 1:
                    left = stack[-1]
                    if height[left] < height[right]:
                        stack.pop(-1)
                    else:
                        break
                left = stack[-1]
                min_h = min(height[left], height[right])
                for i in range(left+1, right):
                    ans += max(min_h - height[i], 0)
                    height[i] = min_h
                if len(stack) == 1 and height[stack[-1]] < height[right]:
                    stack = [right]
                elif height[right] <= height[stack[-1]]:
                    stack.append(right)
                        
            right += 1
        
        return ans
                    
                
                
                    
                    
        