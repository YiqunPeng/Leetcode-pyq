class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = [0] * 26
        v = [False] * 26
        
        for c in s:
            dic[ord(c)-ord('a')] += 1
        
        stack = []
        for c in s:
            dic[ord(c)-ord('a')] -= 1
            
            if not v[ord(c)-ord('a')]:
                while stack and ord(stack[-1]) > ord(c) and dic[ord(stack[-1])-ord('a')] > 0:
                    v[ord(stack.pop(-1))-ord('a')] = False
            
                stack.append(c)
                v[ord(c)-ord('a')] = True
                
        
        ans = ''
        while stack:
            ans = stack.pop(-1) + ans
        return ans
        