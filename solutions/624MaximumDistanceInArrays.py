class Solution:
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        if not arrays: return 0
        
        ans = -sys.maxsize
        
        min_v, max_v = arrays[0][0], arrays[0][-1]
        for i in range(1, len(arrays)):
            if not arrays[i]: continue
            ans = max(ans, abs(max_v-arrays[i][0]), abs(arrays[i][-1]-min_v))
            min_v = min(min_v, arrays[i][0])
            max_v = max(max_v, arrays[i][-1])
        
        return ans