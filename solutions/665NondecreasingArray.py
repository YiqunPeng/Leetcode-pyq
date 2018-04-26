class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) <= 2: return True
        for i in xrange(len(nums)-2):
            n1, n2, n3 = nums[i], nums[i+1], nums[i+2]
            if n1 <= n2 and n2 <= n3: continue
            if n1 > n2 and n2 > n3: return False
            if n1 <= n2 and n2 > n3 and n3 > n1: 
                nums[i+1] = nums[i]
                break
            elif n1 <= n2 and n2 > n3 and n3 < n1:
                nums[i+2] = nums[i+1]
                break
            elif n1 > n2 and n2 <= n3 and n3 < n1:
                nums[i] = nums[i+1]
                break
            elif n1 > n2 and n2 < n3 and n3 > n1:
                nums[i] = nums[i+1]
                break
        for i in xrange(len(nums)-1):
            if nums[i] > nums[i+1]:
                return False
        return True