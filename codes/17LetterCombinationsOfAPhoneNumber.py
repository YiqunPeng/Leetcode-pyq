class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def combination(ans, m, d, index, d_len, s):
            if index == d_len:
                ans.append(s)
                return
            letters = m[int(d[index])]
            for l in letters:
                combination(ans, m, d, index+1, d_len, s+l)
        
        
        if not digits:
            return []
        for d in digits:
            if int(d) == 0 or int(d) == 1:
                return []
        
        ans = []
        mappings = [[],[],
                   ['a','b','c'],['d','e','f'],['g','h','i'],
                   ['j','k','l'],['m','n','o'],['p','q','r','s'],
                   ['t','u','v'],['w','x','y','z']
                  ]
        d_len = len(digits)
        
        combination(ans, mappings, digits, 0, d_len, '')
        
        return ans
        