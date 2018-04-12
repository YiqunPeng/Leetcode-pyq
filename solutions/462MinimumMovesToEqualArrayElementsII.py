class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        median = sorted(nums)[len(nums)/2]
        return sum([abs(nums[i]-median) for i in xrange(len(nums))])