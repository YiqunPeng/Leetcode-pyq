class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right, zero = 0, 0, -1
        nums_len = len(nums)
        ans = -1
        
        while right < nums_len:
            if nums[right] == 0:
                if zero != -1:
                    ans = max(ans, right-left)
                    left = zero + 1
                zero = right
            right += 1
         
        return max(ans, right-left)
                
            
        