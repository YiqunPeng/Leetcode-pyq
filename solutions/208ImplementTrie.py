class TrieNode:
    
    def __init__(self, val):
        self.val = val
        self.children = [None] * 26
        self.is_word = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode('')
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur_node = self.root
        for c in word:
            pos = ord(c) - ord('a')
            if cur_node.children[pos]:
                cur_node = cur_node.children[pos]
                continue
            else:
                new_node = TrieNode(c)
                cur_node.children[pos] = new_node
                cur_node = new_node
        cur_node.is_word = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur_node = self.root
        for c in word:
            pos = ord(c) - ord('a')
            if cur_node.children[pos]:
                cur_node = cur_node.children[pos]
                continue
            else:
                return False
        if not cur_node.is_word:
            return False
        else:
            return True
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur_node = self.root
        for c in prefix:
            pos = ord(c) - ord('a')
            if cur_node.children[pos]:
                cur_node = cur_node.children[pos]
                continue
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)