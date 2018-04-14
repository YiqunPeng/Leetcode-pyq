class Solution:
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        def reverse(str, s, e):
            l, r = s, e
            while l < r:
                temp = str[l]
                str[l] = str[r]
                str[r] = temp
                l += 1
                r -= 1
                
        reverse(str, 0, len(str)-1)
        start = 0
        for i in range(len(str)):
            if str[i] == ' ':
                reverse(str, start, i-1)
                start = i + 1
        
        reverse(str, start, len(str)-1)
        
        