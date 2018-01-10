class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = []
        

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        max_len = -1
        for word in dict:
            if len(word) > max_len:
                max_len = len(word)
        for i in range(max_len):
            self.dic.append([])
        for word in dict:
            l = len(word) - 1
            self.dic[l].append(word)
        

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        if len(word) > len(self.dic):
            return False
        word_list = self.dic[len(word)-1]
        for w in word_list:
            flag = 1
            for i in range(len(word)):
                if word[i] != w[i]:
                    flag -= 1
                if flag < 0:
                    break
            if flag == 0:
                return True
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)