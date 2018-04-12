class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        pali_dict = {}
        ans = 0
        for c in s:
            if pali_dict.has_key(c):
                pali_dict[c] += 1
            else:
                pali_dict[c] = 1
        has_odd = 0
        for key in pali_dict:
            if pali_dict[key] % 2 == 1:
                has_odd = 1
                ans += pali_dict[key] - 1
            if pali_dict[key] % 2 == 0:
                ans += pali_dict[key]
        return ans + has_odd