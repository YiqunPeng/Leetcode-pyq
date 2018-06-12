class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs = sorted(pairs, key=lambda x: x[1], reverse=False)

        e = pairs[0][1]
        ans = 1
        
        for i in range(len(pairs)):
            if pairs[i][0] > e:
                ans += 1
                e = pairs[i][1]
                
        return ans
            