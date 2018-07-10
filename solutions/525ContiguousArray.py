class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        
        dic = {0: 0}
        count = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                count -= 1
            
            if count in dic:
                ans = max(ans, i - dic[count] + 1)
            else:
                dic[count] = i + 1
        
        return ans