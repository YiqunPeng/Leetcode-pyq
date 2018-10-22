class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mod_dict = {0: -1}
        
        s = 0
        for i, num in enumerate(nums):
            s += num
            if k != 0:
                mod = s % k
            else:
                mod = s
            if mod in mod_dict:
                if i - mod_dict[mod] >= 2:
                    return True
            else:
                mod_dict[mod] = i
        
        return False  