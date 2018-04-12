class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        p = len(num1) - 1
        q = len(num2) - 1
        flag = 0
        ans = ''
        
        while p >=0 or q >= 0:
            a = 0 if p < 0 else ord(num1[p]) - ord('0')
            b = 0 if q < 0 else ord(num2[q]) - ord('0')
            add = a + b + flag
            ans = chr(add%10 + ord('0')) + ans
            if add > 9:
                flag = 1
            else:
                flag = 0
            p -= 1
            q -= 1
        
        return ans if flag == 0 else '1' + ans