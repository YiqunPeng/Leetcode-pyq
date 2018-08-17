class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = set()
        self.near = collections.defaultdict(int)
    
    def magic(self, word):
        res = []
        for i in range(len(word)):
            res.append(word[:i] + '*' + word[i+1:])
        return res
    
    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.words = set(dict)
        for word in self.words:
            for m in self.magic(word):
                self.near[m] += 1

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for m in self.magic(word):
            if self.near[m] > 1 or (self.near[m] == 1 and word not in self.words):
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)