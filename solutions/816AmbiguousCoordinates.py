class Solution:
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def is_valid(s):
            if s[0] == '0' and len(s) > 1:
                return False
            return True
        
        def is_valid_decimal(s):
            if s[-1] == '0':
                return False
            return True
            
        
        def add_decimal(s):
            n = len(s)
            res = []
            for i in range(1, n+1):
                if i != n:
                    if is_valid(s[0:i]) and is_valid_decimal(s[i:n]):
                        res.append(s[0:i] + '.' + s[i:n])
                else:
                    if is_valid(s):
                        res.append(s)
            return res
        
        
        S = S[1:-1]
        s_len = len(S)
        
        ans = []
        
        for i in range(1, s_len):
            left, right = S[0:i], S[i: s_len]
            
            l_div = add_decimal(left)
            r_div = add_decimal(right)
            
            for l in l_div:
                for r in r_div:
                    str = '(' + l + ', ' + r + ')'
                    ans.append(str)
            
        return ans