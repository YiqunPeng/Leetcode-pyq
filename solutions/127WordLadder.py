class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        
        list_len = len(wordList)
        word_len = len(beginWord)
                
        q = collections.deque([(beginWord, 1)])
        
        while q:
            w, d = q.popleft()
            
            if w == endWord:
                return d
            
            for i in range(word_len):
                for c in string.ascii_lowercase:
                    n_word = w[0:i] + c + w[i+1:]
                    if n_word in wordList:
                        wordList.remove(n_word)
                        q.append((n_word, d+1))

        return 0