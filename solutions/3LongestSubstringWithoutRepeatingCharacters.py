class Solution:
    # two pointer + hash table
    # time: O(n)
    # space: O(n)
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        
        ans = 1
        s_len = len(s)
        
        left, right = 0, 1
        dic = {s[0]: 0}
        
        while right < s_len:
            if s[right] in dic:
                last = dic[s[right]]
                for i in range(left, last + 1):
                    del dic[s[i]] 
                ans = max(ans, right - left)
                left = last + 1
            dic[s[right]] = right
            right += 1
        
        return max(ans, len(s) - left)
