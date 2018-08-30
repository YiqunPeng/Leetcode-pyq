class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        nums = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        
        ans = ''  
        stack = []
        
        pos = 0
        cnt = 0
        string = ''
        while pos < len(s):
            if not stack:
                ans = ans + string
                string = ''
            
            if s[pos] in nums:
                cnt = cnt * 10 + int(s[pos])
            elif s[pos] == '[':
                stack.append(string[:])
                stack.append(cnt)
                cnt = 0
                string = ''
            elif s[pos] == ']':
                string = string * stack.pop()
                string = stack.pop() + string
                    
            else:
                string = string + s[pos]
            
            pos += 1
        
        if not stack: ans = ans + string
        return ans