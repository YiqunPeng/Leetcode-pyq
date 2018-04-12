class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0]
        for i in xrange(1, num+1):
            if i % 2 == 0:
                ans.append(ans[i/2])
            else:
                ans.append(ans[i-1]+1)
        return ans
        