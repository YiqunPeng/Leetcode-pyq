class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        word = ''
        for c in s:
            if c == ' ' and word:
                stack.append(word)
                word = ''
            elif c != ' ':
                word += c
        if word: stack.append(word)
        
        ans = stack.pop() if stack else ''
        while stack:
            ans = ans + ' ' + stack.pop()
        return ans
                    
            