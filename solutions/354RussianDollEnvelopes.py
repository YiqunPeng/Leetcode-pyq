class Solution:
    # binary search, sort
    # time: O(nlogn)
    # space: O(n)
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes: return 0
        envelopes = sorted(envelopes, key=lambda x:(x[0], -x[1]))
        tail = [sys.maxsize for i in range(len(envelopes))]
        
        size = 0
        for e in envelopes:
            h = e[1]
            
            l, r = 0, size
            pos = -1
            while l <= r:
                m = l + (r - l) // 2
                if (m == 0 and tail[m] >= h) or (tail[m-1] < h <= tail[m]):
                    pos = m
                    break
                elif tail[m] < h:
                    l = m + 1
                else:
                    r = m - 1
            
            if pos == -1:
                size += 1
                tail[size] = h
            else:
                tail[pos] = h
                
        return size + 1
        
    
    # TLE, 80/85 cases passed
    # dp
    # time: O(n^2)
    # space: O(n)
    # def maxEnvelopes(self, envelopes):
    #     """
    #     :type envelopes: List[List[int]]
    #     :rtype: int
    #     """
    #     if not envelopes: return 0

    #     envelopes = sorted(envelopes, key=lambda x: (x[0], x[1]))
    #     dp = [1] * len(envelopes)

    #     for i in range(len(envelopes)):
    #         ei = envelopes[i]
    #         for j in range(0, i):
    #             ej = envelopes[j]
    #             if ei[0] > ej[0] and ei[1] > ej[1]:
    #                 dp[i] = max(dp[i], dp[j] + 1)

    #     return max(dp)
