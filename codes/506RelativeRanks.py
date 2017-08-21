class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        p_dict = {}
        for i in xrange(len(nums)):
            p_dict[str(i)] = nums[i]
        sorted_list = sorted(p_dict.items(), key=lambda item:item[1], reverse=True)
        for i in xrange(len(sorted_list)):
            index = int(sorted_list[i][0])
            if i == 0:
                nums[index] = 'Gold Medal'
            elif i == 1:
                nums[index] = 'Silver Medal'
            elif i == 2:
                nums[index] = 'Bronze Medal'
            else:
                nums[index] = str(i + 1) 
        return nums