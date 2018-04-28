class Solution:
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        def find_pattern(s):
            pattern = []
            for i in range(1, len(s)):
                pattern.append((ord(s[i]) - ord(s[i-1])) % 26)
            return tuple(pattern)
        
        
        dic = {}
        
        for s in strings:
            pattern = find_pattern(s)
            if pattern in dic:
                dic[pattern].append(s)
            else:
                dic[pattern] = [s]
                
        ans = []
        for item in dic.values():
            ans.append(item)
        
        return ans