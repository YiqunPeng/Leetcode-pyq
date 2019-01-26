class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2: return 0
        
        min_val, max_val = min(nums), max(nums)
        if min_val == max_val: return 0
        
        gap = (max_val - min_val) // (n - 1) or 1
        buckets = [[None, None] for i in range((max_val - min_val) // gap + 1)]
        
        for num in nums:
            bucket = buckets[(num - min_val) // gap]         
            bucket[0] = num if bucket[0] is None else min(bucket[0], num)
            bucket[1] = num if bucket[1] is None else max(bucket[1], num)
            
        buckets = [b for b in buckets if b[0] is not None]
        ans = 0
        for i in range(1, len(buckets)):
            ans = max(ans, buckets[i][0] - buckets[i-1][1])
        return ans