class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) <= 2: return 0
        diffs = [A[i+1]-A[i] for i in xrange(len(A)-1)]
        ans, cnt = 0, 1
        diff = diffs[0]
        for i in xrange(1, len(diffs)):
            if diff == diffs[i]:
                cnt += 1
            else:
                if cnt >= 2:
                    ans += (cnt * (cnt-1)) / 2
                cnt = 1
                diff = diffs[i]
        return ans + (cnt * (cnt-1)) / 2