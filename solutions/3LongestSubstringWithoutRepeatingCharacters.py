class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        ans = 1
        s_len = len(s)

        left, right = 0, 1
        dic = {s[0]: 0}

        while right < s_len:
            if s[right] == s[left]:
                dic[s[left]] = right
                left += 1
                right += 1
                continue
            if s[right] in dic:
                ans = max(ans, right-left)
                left = dic[s[right]] + 1
                right = left + 1
                dic = {}
            else:
                dic[s[right]] = right
                right += 1

        return max(ans, len(s)-left)
