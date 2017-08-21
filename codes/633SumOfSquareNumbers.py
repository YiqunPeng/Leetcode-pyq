class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left, right = 0, int(math.sqrt(c))
        
        while left <= right:
            temp = left ** 2 + right ** 2
            if temp == c:
                return True
            elif temp < c:
                left += 1
            else:
                right -= 1
        
        return False
            