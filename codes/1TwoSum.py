class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in xrange(len(nums)):
            sub = target - nums[i]
            if dic.has_key(sub):
                return [i, dic[sub]]
            else:
                dic[nums[i]] = i
                
        
        