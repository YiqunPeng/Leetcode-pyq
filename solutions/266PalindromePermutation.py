class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_set = set()
        
        for c in s:
            if c not in s_set:
                s_set.add(c)
            else:
                s_set.remove(c)
        
        return len(s_set) <= 1