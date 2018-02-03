class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        nums_len = len(nums)
        
        for i in range(nums_len-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            l, r = i+1, nums_len-1
            while l < r:
                s = nums[l] + nums[r] + nums[i]
                if s == 0:
                    ans.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < nums_len-1:
                        l += 1
                    while nums[r] == nums[r+1] and r > i:
                        r -= 1
                elif s > 0:
                    r -= 1
                else:
                    l += 1
        
        return ans
            
                                
        
        
        