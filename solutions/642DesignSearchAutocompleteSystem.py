class TrieNode:
    
    def __init__(self, val = ''):
        self.val = val
        self.counter = collections.defaultdict(int)
        self.children = {}

        
class AutocompleteSystem:

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.trie = TrieNode()
        self.query = ''
        
        for i in range(len(sentences)):
            self.add_to_trie(sentences[i], times[i])
        
        
    def add_to_trie(self, sentence, time):
        root = self.trie
        
        for char in sentence:
            if char not in root.children:
                root.children[char] = TrieNode(char)
            root = root.children[char]
            root.counter[sentence] += time
            
            
    def search_in_trie(self, sentence):
        root = self.trie
        
        for char in sentence:
            if char not in root.children:
                return {}
            root = root.children[char]
            
        return root.counter
    

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == '#':
            self.add_to_trie(self.query, 1)
            self.query = ''
            return []
        
        self.query += c     
        result = self.search_in_trie(self.query)

        return [i[0] for i in sorted(result.items(), key=lambda x:(-x[1], x[0]))[:3]]
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)