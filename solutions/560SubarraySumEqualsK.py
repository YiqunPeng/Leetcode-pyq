class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        
        pre_dict = collections.defaultdict(int)
        pre_dict[0] = 1
        pre = 0
        
        for i in range(len(nums)):
            pre += nums[i]
            d = pre - k
            ans += pre_dict[d]
            pre_dict[pre] += 1
        
        return ans
