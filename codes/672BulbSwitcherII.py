class Solution(object):
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        odd = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],
              [0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]]
        even = [[0,0,0,0],[1,1,1,1],[1,1,0,0],[1,0,1,0],
                [1,0,0,1],[0,1,1,0],[0,1,0,1],[0,0,1,1]]
        if m % 2 == 0:
            modes = even
        else:
            modes = odd
            
        res = []
        for mode in modes:
            if sum(mode) > m:
                continue
            bulbs = [1 for i in range(n)]
            if mode[0] == 1:
                bulbs = [1-bulbs[i] for i in range(n)]
            if mode[1] == 1:
                for i in range(n):
                    if i % 2 == 1:
                        bulbs[i] = 1 - bulbs[i]
            if mode[2] == 1:
                for i in range(n):
                    if i % 2 == 0:
                        bulbs[i] = 1 - bulbs[i]         
            if mode[3] == 1:
                for i in range(n):
                    if i % 3 == 0:
                        bulbs[i] = 1 - bulbs[i]
            res.append(tuple(bulbs))
            
        return len(set(res))