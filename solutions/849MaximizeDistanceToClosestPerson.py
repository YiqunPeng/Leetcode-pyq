class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        ans = 0
        pre = -1
        
        for i in range(len(seats)):
            if seats[i] == 1:
                if pre == -1:
                    ans = max(ans, i)
                else:
                    ans = max(ans, (i-pre)//2)
                pre = i
        
        if seats[-1] == 0:
            ans = max(ans, len(seats)-1-pre)
            
        return ans
        
        