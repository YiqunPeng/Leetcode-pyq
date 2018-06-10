class Solution:
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        ans = []
        
        def backtracking(word, curr):
            if not word:
                ans.append(curr)
            for i in range(1, len(word)+1):
                if curr:
                    if curr[-1] in string.digits:
                        backtracking(word[i:], curr+word[:i])
                    else:
                        backtracking(word[i:], curr+str(i))
                else:
                    backtracking(word[i:], curr+word[:i])
                    backtracking(word[i:], curr+str(i))

        backtracking(word, '')
        return ans