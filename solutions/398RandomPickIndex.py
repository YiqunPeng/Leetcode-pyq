class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = copy.deepcopy(nums)
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        ans = -1
        nums = self.nums
        cnt = 0
        
        for i in range(len(nums)):
            if nums[i] != target:
                continue
            cnt += 1
            if ans == -1:
                ans = i
                continue
            if int(random.uniform(0, cnt)) == 0:
                ans = i
        
        return ans