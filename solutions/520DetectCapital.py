class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) <= 1:
            return True
        
        c = word[1]
        
        if c >= 'a' and c <= 'z':
            flag = 1
        else:
            flag = 2

        if flag == 1:
            for letter in word[2:]:
                if letter >= 'A' and letter <= 'Z':
                    return False
        
        if flag == 2:
            for letter in word:
                if letter >= 'a' and letter <= 'z':
                    return False
            
        return True