class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def n_sum(nums, N, target, res, ans):
            n_len = len(nums)
            if n_len < N or target > nums[-1] * N or target < nums[0] * N:
                return
            
            if N == 2:
                l, r = 0, n_len - 1
                while l < r:
                    v = nums[l] + nums[r]
                    if v == target:
                        ans.append(res + [nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif v > target:
                        r -= 1
                    else:
                        l += 1
            else:
                for i in range(n_len - N + 1):
                    if i == 0 or i > 0 and nums[i] != nums[i-1]:
                        n_sum(nums[i+1:], N-1, target-nums[i], res+[nums[i]], ans)
        
        
        ans = []
        n_sum(sorted(nums), 4, target, [], ans)
        return ans