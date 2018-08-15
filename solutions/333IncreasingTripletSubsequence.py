class Solution:
    
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        f, s = sys.maxsize, sys.maxsize
        for num in nums:
            if num <= f:
                f = num
            elif num <= s:
                s = num
            else:
                return True
        
        return False
