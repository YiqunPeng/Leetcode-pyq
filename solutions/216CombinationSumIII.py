class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def backtracking(nums, curr, curr_sum):
            if len(curr) + 1 == k:
                if nums and nums[0] <= n - curr_sum <= 9:
                    ans.append(curr + [n - curr_sum])
            else:
                for i in range(len(nums)):
                    if curr_sum + nums[i] < n:
                        backtracking(nums[i+1:], curr + [nums[i]], curr_sum + nums[i])
                    else:
                        break

                        
        ans = []
        backtracking(range(1, 10), [], 0)
        return ans