class Solution:

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.r = radius
        self.x, self.y = x_center, y_center
        self.pi = 3.141592
        

    def randPoint(self):
        """
        :rtype: List[float]
        """
        r_random = random.random() ** 0.5 * self.r        
        degree = random.random() * 2 * self.pi
        
        return [math.cos(degree) * r_random + self.x, math.sin(degree) * r_random + self.y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()