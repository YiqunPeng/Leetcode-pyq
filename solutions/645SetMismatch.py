class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        marks = [0] * (max(nums) + 1)
        
        for num in nums:
            if marks[num] == 0:
                marks[num] = 1
            else:
                return [num, int(0.5*(1+n)*n-sum(nums))+num]