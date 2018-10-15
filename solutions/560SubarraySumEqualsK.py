class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        
        pre_sum = 0
        pre_dict = collections.defaultdict(int)
        pre_dict[0] = 1
        
        for i in range(len(nums)):
            pre_sum += nums[i]
            d = pre_sum - k
            ans += pre_dict[d]
            pre_dict[pre_sum] += 1
        
        return ans        