class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations: return 0
        if len(citations) == 1: return min(1, citations[0])
        
        c = citations[::-1]
        
        for i in range(len(c)):
            if c[i] <= i:
                return i
            
        return len(c)