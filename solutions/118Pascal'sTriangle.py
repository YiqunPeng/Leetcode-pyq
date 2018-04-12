class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        for i in xrange(numRows):
            row = []
            for j in xrange(i+1):
                if j == 0 or j == i:
                    row.append(1)
                    continue
                row.append(ans[i-1][j-1] + ans[i-1][j])
            ans.append(row)
        
        return ans