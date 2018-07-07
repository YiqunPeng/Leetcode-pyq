class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        s_len = len(s)
        if s_len <= k: return s_len
        
        dic = {}
        for i in range(k):
            dic[s[i]] = dic.get(s[i], 0) + 1
                
        ans = k
        
        left, right = 0, k  
        while left < right < s_len:
            if s[right] in dic:
                dic[s[right]] += 1
                ans = max(ans, right-left+1)
            else:
                if len(dic) < k:
                    dic[s[right]] = 1
                else:
                    while len(dic) != k - 1:
                        dic[s[left]] -= 1
                        if dic[s[left]] == 0: del dic[s[left]]
                        left += 1
                    dic[s[right]] = 1
                ans = max(ans, right-left+1)
            right += 1
        
        return ans
        
