class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        words = S.split(' ')
        
        ans = ''
        pos = 1
        for word in words:
            if word[0] in vowels:
                ans = ans + word + 'ma' + 'a' * pos + ' '
            else:
                ans = ans + word[1:] + word[0] + 'ma' + 'a' * pos + ' '
            pos += 1
        
        return ans[:-1]

                
        