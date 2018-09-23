class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = []
        if not nums: return ans
        
        start = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                if i == start + 1:
                    ans.append(str(nums[start]))
                else:
                    ans.append(str(nums[start]) + '->' + str(nums[i-1]))
                start = i
        
        if start + 1 == len(nums):
            ans.append(str(nums[start]))
        else:
            ans.append(str(nums[start]) + '->' + str(nums[-1]))
        return ans