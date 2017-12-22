class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        ans = ''
        length = 0
        dic = {}
        licensePlate = licensePlate.lower()
        
        for l in licensePlate:
            if l >= 'a' and l <= 'z':
                dic[l] = dic.get(l, 0) + 1
                length += 1

        for w in words:
            if ans != '' and len(w) >= len(ans): continue
            found = 1
            w_dic = {}
            for l in w:
                if l >= 'a' and l <= 'z':
                    w_dic[l] = w_dic.get(l, 0) + 1
            for (key, value) in dic.items():
                if w_dic.get(key, 0) < value:
                    found = 0
                    break
            if found == 1:
                ans = w
        
        return ans