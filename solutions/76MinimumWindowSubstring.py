class Solution:
    # hash table + two pointer
    # time: O(n)
    # space: O(k) k == len(t)
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s: return ''
        if not t: return s[0]
        
        ans = [0, len(s)-1]      
        t_dict = collections.defaultdict(int)
        for c in t:
            t_dict[c] += 1
        s_dict = collections.defaultdict(int)
        
        left, right = 0, 0
        cover_flag = False
        while right < len(s):
            if s[right] in t_dict:
                s_dict[s[right]] += 1
                while s[left] not in t_dict or s_dict[s[left]] > t_dict[s[left]]:
                    if s[left] in t_dict: s_dict[s[left]] -= 1
                    left += 1
                if not cover_flag:
                    cover_flag = all([s_dict[key] >= t_dict[key] for key in t_dict])
                if cover_flag:
                    if right - left < ans[1] - ans[0]:
                        ans[0], ans[1] = left, right
                    if ans[1] - ans[0] + 1 == len(t): return s[ans[0]:ans[1]+1]
            right += 1
        
        return s[ans[0]:ans[1]+1] if cover_flag else ''
    
