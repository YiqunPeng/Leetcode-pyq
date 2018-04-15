class ValidWordAbbr:

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.word_list = list(set(dictionary))
        self.dic = {}
        for word in self.word_list:
            if len(word) <= 2: 
                self.dic[word] = self.dic.get(word, 0) + 1
            else:    
                abbr = word[0] + str(len(word)-2) + word[-1]
                self.dic[abbr] = self.dic.get(abbr, 0) + 1
        # print(self.dic)
        

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        abbr = ''
        if len(word) <= 2:
            abbr = word
        else:
            abbr = word[0] + str(len(word)-2) + word[-1]
        
        if word in self.word_list:
            if self.dic[abbr] > 1:
                return False
            else:
                return True
        else:
            if abbr in self.dic and self.dic[abbr] > 0:
                return False
            else:
                return True
        

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)