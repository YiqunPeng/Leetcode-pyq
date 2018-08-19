class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        ans = []
        
        for word in words:
            w2p = collections.defaultdict(str)
            p2w = collections.defaultdict(str)
            
            if len(word) != len(pattern): continue
            flag = True
            
            for i in range(len(word)):
                if word[i] not in w2p:
                    w2p[word[i]] = pattern[i]
                elif w2p[word[i]] != pattern[i]:
                    flag = False
                    break
                if pattern[i] not in p2w:
                    p2w[pattern[i]] = word[i]
                elif p2w[pattern[i]] != word[i]:
                    flag = False
                    break
            
            if flag: 
                ans.append(word)
        
        return ans
                
                    