class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr: return 0
        
        ans = 0
        max_pos = 0
        
        for i in range(len(arr)):
            max_pos = max(arr[i], max_pos)
            if i == max_pos:
                ans += 1
        
        return ans
        