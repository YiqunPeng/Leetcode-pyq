class Solution:
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums: return 0
        n = len(nums)      
        
        prefix = [0] * n
        prefix[0] = nums[0]
        sum_dict = collections.defaultdict(list)
        sum_dict[0] = [-1]
        sum_dict[prefix[0]].append(0)
        for i in range(1, n):
            prefix[i] = prefix[i-1] + nums[i]
            sum_dict[prefix[i]].append(i)
        
        ans = 0
        for key, val in sum_dict.items():
            d = key - k
            if d in sum_dict:
                if val[-1] >= sum_dict[d][0]:
                    ans = max(ans, val[-1] - sum_dict[d][0])
        return ans