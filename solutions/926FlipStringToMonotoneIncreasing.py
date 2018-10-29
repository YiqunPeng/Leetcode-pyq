class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        one_cnt = 0
        for s in S:
            if s == '1':
                one_cnt += 1
        
        ans = one_cnt
        zero_cnt = 0
        for s in S[::-1]:
            if s == '0':
                zero_cnt += 1
            else:
                one_cnt -= 1
                ans = min(ans, zero_cnt + one_cnt)
        return ans