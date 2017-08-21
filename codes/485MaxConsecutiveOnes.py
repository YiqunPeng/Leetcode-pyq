class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        temp = 0
        
        for num in nums:
            if num == 1:
                temp += 1
            if num == 0:
                if temp > ans:
                    ans = temp
                temp = 0
        
        return max(temp, ans)