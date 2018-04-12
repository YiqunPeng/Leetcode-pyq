class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {}
        
        for c in s:
            dic[c] = dic.get(c, 0) + 1
        
        odd = 0
        for key in dic:
            if dic[key] % 2 == 1:
                odd += 1
                if odd > 1:
                    return False
        
        return True