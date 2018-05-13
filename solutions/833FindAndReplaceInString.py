class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """        
        index, s, t = indexes, sources, targets
        
        dic = {}
        for i in range(len(index)):
            dic[index[i]] = [s[i], t[i]]
        dic = sorted(dic.items())[::-1]
        
        for i in dic:
            so, ta, key = i[1][0], i[1][1], i[0]
            if S[key : key+len(so)] == so:
                S = S[0:key] + ta + S[key+len(so):]
                
        return S