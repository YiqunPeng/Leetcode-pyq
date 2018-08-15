class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        ans = [[r0, c0]]
        
        x, y = r0, c0
        ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        s = 1
        d = 0
        cnt_s = 0
        
        while len(ans) < R * C:
            cnt_s += 1
            t_s = s
            for i in range(t_s):
                x = x + ds[d][0]
                y = y + ds[d][1]
                if 0 <= x < R and 0 <= y < C:
                    ans.append([x, y])
            d = (d + 1) % 4
            if cnt_s == 2:
                s += 1
                cnt_s = 0
        
        return ans
        