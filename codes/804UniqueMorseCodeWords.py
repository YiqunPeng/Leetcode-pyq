class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        mappings = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        codes = []
        for word in words:
            code = ""
            for l in word:
                code = code + mappings[ord(l)-ord('a')]
            codes.append(code)
        
        return len(set(codes))