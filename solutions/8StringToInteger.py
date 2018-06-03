class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str: return 0
        
        min_v, max_v = -2 ** 31, 2 ** 31 - 1
        
        while str and str[0] == ' ':
            str = str[1:]
            
        ans = 0
        sig = 1
    
        if not str: return 0
    
        if str[0] == '-':
            sig = -1
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]
        
        if not str or str[0] not in string.digits:
            return 0
        
        while str and str[0] in string.digits:
            ans = ans * 10 + int(str[0])
            str = str[1:]
        
        ans = ans * sig
        
        if ans < 0:
            return max(min_v, ans)
        else:
            return min(max_v, ans)
        
        