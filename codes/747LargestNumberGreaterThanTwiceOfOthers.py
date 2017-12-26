class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fi, sec = 0, -1
        
        if len(nums) == 1: return 0
        
        for i in range(1, len(nums)):
            if nums[i] >= nums[fi]:
                sec = fi
                fi = i
            elif nums[i] > nums[sec]:
                sec = i
                
        if nums[fi] >= 2 * nums[sec]:
            return fi
        else:
            return -1
        