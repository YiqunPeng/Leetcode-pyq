class Solution:
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        n = len(sentence)
        dp = [-1] * n
        
        for i in range(n):
            length = 0
            pos = i
            
            while length + len(sentence[pos % n]) <= cols:
                length = length + len(sentence[pos % n]) + 1
                pos += 1
            
            dp[i] = pos

        words = 0
        k = 0
        for i in range(rows):
            words += dp[k] - k
            k = dp[k] % n
        
        return words // n