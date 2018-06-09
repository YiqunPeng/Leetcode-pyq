class Solution:
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        word_p, abbr_p = 0, 0
        v = 0
        while word_p < len(word) and abbr_p < len(abbr):
            if abbr[abbr_p] in string.digits:
                if abbr[abbr_p] == '0' and v == 0: return False
                v = v * 10 + int(abbr[abbr_p])
                abbr_p += 1
                continue
            else:
                if v != 0:
                    word_p += v
                    v = 0
                    continue
                else:
                    if word[word_p] != abbr[abbr_p]:
                        return False
                    else:
                        word_p += 1
                        abbr_p += 1
        
        return word_p + v == len(word) and abbr_p == len(abbr)
