class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        
        for a in asteroids:
            if a > 0: 
                stack.append(a)
            else:
                while stack and stack[-1] > 0 and stack[-1] + a < 0:
                    stack.pop()
                if stack and stack[-1] + a == 0:
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(a)
        
        return stack