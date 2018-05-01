class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        def dfs(s, pos, stack):
            res = ''
            val = 0
            while pos < len(s):
                if 0 <= ord(s[pos])-ord('0') <= 9:
                    val = val * 10 + int(s[pos])
                elif s[pos] == '[':
                    str, pos = dfs(s, pos+1, stack+[val])
                    res += str
                    val = 0
                elif s[pos] == ']':
                    return res * stack.pop(-1), pos
                else:
                    res += s[pos]
                pos += 1
            return res, pos
                
               
        ans = ''
        val, pos = 0, 0
        
        while pos < len(s):
            if 0 <= ord(s[pos])-ord('0') <= 9:
                val = val * 10 + int(s[pos])
            elif s[pos] == '[':
                res, pos = dfs(s, pos+1, [val])
                ans += res 
                val = 0
            else:
                ans += s[pos]
            pos += 1
        
        return ans