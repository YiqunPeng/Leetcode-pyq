class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sums = []
        if nums == []: return
        self.sums.append(nums[0])
        for i in xrange(1, len(nums)):
            self.sums.append(self.sums[i-1] + nums[i])
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j] - (self.sums[i-1] if i-1>=0 else 0)