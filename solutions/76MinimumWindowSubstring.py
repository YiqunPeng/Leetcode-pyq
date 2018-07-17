class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        def contain_all(s_d, t_d):
            for key in t_d:
                if key not in s_d or t_d[key] > s_d[key]:
                    return False
            return True
            
    
        if not s: return ''
        if not t: return s[0]
    
        t_dic = {}
        for i in t:
            t_dic[i] = t_dic.get(i, 0) + 1
        
        s_dic = {}
        pos = 0
        left, right = -1, -1
        while pos < len(s):
            if s[pos] not in t_dic:
                pos += 1
                continue
            else:
                if left == -1: left = pos
                s_dic[s[pos]] = s_dic.get(s[pos], 0) + 1
                while s[left] not in t_dic or s_dic[s[left]] > t_dic[s[left]]:
                    if s[left] in t_dic:
                        s_dic[s[left]] -= 1
                    left += 1
                if contain_all(s_dic, t_dic):
                    pos += 1
                    break
                pos += 1

        right = pos
        if not contain_all(s_dic, t_dic): return ''
        ans = s[left:right]
        if right == len(s): return ans
        
        while right < len(s):
            if s[right] not in t_dic:
                right += 1
                continue
            else:
                if s[right] == s[left]:
                    s_dic[s[right]] += 1
                    while s[left] not in t_dic or s_dic[s[left]] > t_dic[s[left]]:
                        if s[left] in t_dic:
                            s_dic[s[left]] -= 1
                        left += 1
                    if right - left + 1 < len(ans):
                        ans = s[left:right+1]
                        if len(ans) == len(t): return ans            
                else:
                    s_dic[s[right]] += 1
                right += 1
        
        return ans
