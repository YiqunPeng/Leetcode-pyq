class TreeNode:
    
    def __init__(self, char):
        self.char = char
        self.children = [None] * 26
        self.is_end = False
        

class Trie:
    
    def __init__(self):
        self.root = TreeNode('')
        
    
    def add_word(self, word):
        node = self.root
        for c in word:
            if not node.children[ord(c) - ord('a')]:
                node.children[ord(c) - ord('a')] = TreeNode(c)
            node = node.children[ord(c) - ord('a')]
        node.is_end = True
                  
    
    def search_prefix(self, word):
        res = ''
        node = self.root
        for c in word:
            if not node.children[ord(c) - ord('a')]:
                return word
            res += c
            if node.children[ord(c) - ord('a')].is_end:
                return res
            else:
                node = node.children[ord(c) - ord('a')]
        return res
                                

class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = Trie()
        for word in dict:
            trie.add_word(word)
        
        words = sentence.split(' ')
        for i in range(len(words)):
            words[i] = trie.search_prefix(words[i])
        return ' '.join(words)