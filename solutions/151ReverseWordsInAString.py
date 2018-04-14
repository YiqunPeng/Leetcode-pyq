class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        
        s_len = len(s)
        pos = 0
        temp = ''
        while pos < s_len:
            if s[pos] == ' ': 
                stack.append(temp)
                temp = ''
            else:
                temp += s[pos]
            pos += 1
        
        stack.append(temp)
        
        ans = ''
        for i in range(len(stack)-1, -1, -1):
            if stack[i] == '': continue
            ans = ans + stack[i] + ' '
        
        if len(ans) > 0 and ans[-1] == ' ':
            return ans[:-1]
        else:
            return ans
            