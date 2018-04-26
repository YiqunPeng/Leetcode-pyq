class TreeNode:
    
    def __init__(self, c):
        self.c = c
        self.child_nodes = {}
        self.is_word = False
        
    def set_is_word(self, val):
        self.is_word = val


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode('')
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.child_nodes:
                node.child_nodes[word[i]] = TreeNode(word[i])
            node = node.child_nodes[word[i]]
            if i == len(word) - 1:
                node.set_is_word(True)
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        nodes = [self.root]
        for i in range(len(word)):
            if word[i] == '.':
                temp_nodes = []
                for node in nodes:
                    for key in node.child_nodes:
                        temp_nodes.append(node.child_nodes[key])
                nodes = temp_nodes
            else:
                temp_nodes = []
                for node in nodes:
                    if word[i] in node.child_nodes:
                        temp_nodes.append(node.child_nodes[word[i]])
                nodes = temp_nodes
        for node in nodes:
            if node.is_word:
                return True
        return False        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)