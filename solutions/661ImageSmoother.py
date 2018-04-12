class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        row, col = len(M), len(M[0])
        ans = [[0]*col for i in xrange(row)]
        for i in xrange(row):
            for j in xrange(col):
                cnt = 0
                val = 0
                for p in xrange(-1, 2):
                    for q in xrange(-1, 2):
                        if ((i+p)<0) or ((i+p)>=row) or ((j+q)<0) or ((j+q)>=col):
                            continue
                        cnt += 1
                        val += M[i+p][j+q]
                ans[i][j] = val / cnt
        return ans
        