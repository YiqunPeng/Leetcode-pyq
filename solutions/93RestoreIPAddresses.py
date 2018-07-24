class Solution:
    # back tracking
    # time: O(3^n)
    # space: O(3^n)
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        if not s: return ans
        
        def backtracking(s, sec, res):
            if not s: return
            if sec == 1:
                if (s == '0' and len(s) == 1) or (1 <= int(s) <= 255 and s[0] != '0'):
                    ans.append(res+s)
                return
            
            if s[0] == '0':
                backtracking(s[1:], sec-1, res+'0.')
            else:
                for i in range(1, 4):
                    if 0 <= int(s[:i]) <= 255:
                        backtracking(s[i:], sec-1, res+s[:i]+'.')
              
        backtracking(s, 4, '')
        return ans 
        