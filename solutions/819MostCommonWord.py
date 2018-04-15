class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.lower()
        symbols = [' ', '!', '?', ',', ';', '.', '\'']
        
        dic = {}
        word = ''
        
        for c in paragraph:
            if c in symbols and word == '': continue
            if c in symbols:
                if word not in banned:
                    dic[word] = dic.get(word, 0) + 1
                word = ''
            else:
                word = word + c
        
        if word != '' and word not in banned:
            dic[word] = dic.get(word, 0) + 1
                    
        ans = ''
        cnt = -1
        
        for key in dic:
            if dic[key] > cnt:
                ans = key
                cnt = dic[key]
        
        return ans
                