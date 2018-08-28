class Solution:
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        n = len(position)
        
        time = [0] * n
        for i in range(n):
            time[i] = (float(target - position[i]) / float(speed[i]), -position[i])
        time.sort(key=lambda x: x[1])
        
        ans = 0
        slow = 0
        for t in time:
            if t[0] > slow:
                ans += 1
                slow = t[0]
        
        return ans