class Solution:
    # hash
    # time: O(n)
    # space: O(n)
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ans = []
        
        s_len, p_len = len(s), len(p)
        
        p_dict = collections.defaultdict(int)
        s_dict = collections.defaultdict(int)
        
        for c in p:
            p_dict[c] += 1
        
        for i in range(s_len):
            pre = i - p_len
            s_dict[s[i]] += 1

            if pre >= 0:
                s_dict[s[pre]] -= 1
                if s_dict[s[pre]] == 0: del s_dict[s[pre]]
            if s_dict == p_dict:
                ans.append(pre + 1)
        
        return ans