class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        ans = ''
        
        max_len = max([len(w) for w in words])
        word_len = max_len
        dic = [[] for i in range(max_len)]
        for w in words:
            dic[len(w)-1].append(w)

        for i in range(1, max_len):
            cnt = len(dic[i])
            for j in range(cnt):
                prefix = dic[i][j][0:-1]
                if prefix not in dic[i-1]:
                    dic[i][j] = ''
            all_empty = 1
            for j in range(cnt):
                if dic[i][j] != '':
                    all_empty = 0
                    break
            if all_empty:
                word_len = i
                break

        return min([w for w in dic[word_len-1] if w != ''])
                
        