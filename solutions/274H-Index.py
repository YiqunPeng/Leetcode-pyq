class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations: return 0
        
        cnt = [0] * (max(citations) + 1)
        
        for c in citations:
            cnt[c] += 1
             
        t = 0
        for i in range(len(cnt)-1, -1, -1):
            t += cnt[i]
            if t >= i:
                return i