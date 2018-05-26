class Solution:
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums: return 0
        
        nums_len = len(nums)
        
        pre = [0] * nums_len
        pre[0] = nums[0]
        
        dic = {pre[0]:[0]}
        
        for i in range(1, nums_len):
            pre[i] = pre[i-1] + nums[i]
            if pre[i] in dic:
                dic[pre[i]].append(i)
            else:
                dic[pre[i]] = [i]
        
        ans = 0
        for key, value in dic.items():
            if key == k:
                ans = max(ans, value[-1] + 1)
            else:
                diff = key - k
                if diff in dic:
                    ans = max(ans, dic[key][-1] - dic[diff][0])
        
        return ans
            
        
        