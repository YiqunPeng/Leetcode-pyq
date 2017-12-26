class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if target >= letters[-1] or target < letters[0]: return letters[0]
        
        for i in range(1, len(letters)):
            if target < letters[i]:
                return letters[i]