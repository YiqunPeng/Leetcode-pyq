class Solution:
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        length = len(dominoes)
        ans = [0] * length
        
        flag = 0
        for i in range(length):
            if dominoes[i] == 'L':
                flag = 0
                continue
            if dominoes[i] == 'R':
                flag = 1
                ans[i] = 1
                if i + 1 < length and dominoes[i+1] == '.':
                    ans[i+1] += 1
            if dominoes[i] == '.' and flag > 0:
                ans[i] += flag / 2.0
                flag = flag / 2.0

        flag = 0
        for i in range(length-1, -1, -1):
            if dominoes[i] == 'R':
                flag = 0
                continue
            if dominoes[i] == 'L':
                flag = 1
                ans[i] = -1
                if i - 1 > 0 and dominoes[i-1] == '.':
                    ans[i-1] -= 1
            if dominoes[i] == '.' and flag > 0:
                ans[i] -= flag / 2.0
                flag = flag / 2.0
         
        res = ''
        for i in ans:
            if i == 0:
               res = res + '.'
            elif i > 0:
                res = res + 'R'
            else:
                res = res + 'L'
        return res