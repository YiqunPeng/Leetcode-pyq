class Solution:
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        dic = {}
        for d in dict:
            if d[0] in dic:
                dic[d[0]].append(d)
            else:
                dic[d[0]] = [d]

        intervals = []
        for i in range(len(s)):
            words = dic[s[i]] if s[i] in dic else []
            for word in words:
                if word == s[i:i+len(word)]:
                    intervals.append([i, i+len(word)])
        
        merged = []
        pos = -1
        for i in intervals:
            s_p, e_p = i[0], i[1]
            if not merged:
                merged = [[s_p, e_p]]
                pos = 0
            else:
                if merged[pos][1] < s_p:
                    merged.append([s_p, e_p])
                    pos += 1
                else:
                    merged[pos] = [merged[pos][0], max(merged[pos][1], e_p)]
        
        if not merged: return s
        
        ans = s[:merged[0][0]]
        for i in range(len(merged)):
            if i > 0:
                ans = ans + s[merged[i-1][1]:merged[i][0]]
            ans = ans + '<b>' + s[merged[i][0]:merged[i][1]] + '</b>'

        return ans + s[merged[-1][1]:]
            
                