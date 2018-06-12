class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_len = len(s)
        if s_len <= 2: return s_len
        
        ans = 0
        
        left, right = 0, 1
        dic = {s[left]: 1}
        
        while left < right and right < s_len:
            if s[right] in dic:
                dic[s[right]] += 1
            else:
                if len(dic.keys()) < 2:
                    dic[s[right]] = 1
                else:
                    ans = max(ans, right - left)
                    while len(dic.keys()) >= 2:
                        if dic[s[left]] == 1:
                            del dic[s[left]]
                        else:
                            dic[s[left]] -= 1
                        left += 1
                    dic[s[right]] = 1
            right += 1
            
        return max(ans, right - left)