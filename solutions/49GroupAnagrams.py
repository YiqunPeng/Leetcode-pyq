class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """              
        def standardize(s):
            t = [0] * 26
            for c in s:
                t[ord(c)-ord('a')] += 1
            res = ''
            for i in range(26):
                if t[i] > 0:
                    res = res + str(ord('a')+i) * t[i]
            return res
        
        ans = []
        group = {}
        
        for s in strs:
            res = standardize(s)
            if res in group:
                pos = group[res]
                ans[pos].append(s)
            else:
                ans.append([s])
                group[res] = len(ans) - 1
        
        return ans
                
                    