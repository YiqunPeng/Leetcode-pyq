class Solution:
    # trie
    # time: O(n * m) n -- number of words, m -- max length of words
    # space: O(n)
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        trie = {}
        
        for w in words:
            w = w[::-1]
            for i in range(len(w) + 1):
                if i != len(w):
                    trie[w[:i]] = 0
                else:
                    if w[:i] not in trie:
                        trie[w[:i]] = len(w) + 1

        return sum(v for v in trie.values())
        
    
    # hash table
    # time: O(n * m) n -- number of words, m -- max length of words
    # space: O(n)
    # def minimumLengthEncoding(self, words):
    #     """
    #     :type words: List[str]
    #     :rtype: int
    #     """
    #     words_set = set(words)

    #     for w in words:
    #         for i in range(1, len(w)):
    #             words_set.discard(w[i:])

    #     return sum(len(w) + 1 for w in words_set)