class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowels_list = []
        
        for c in s:
            if c in vowels:
                vowels_list.append(c)
        pos = len(vowels_list) - 1
        
        s_list = list(s)
        for i in xrange(len(s_list)):
            if s_list[i] in vowels:
                s_list[i] = vowels_list[pos]
                pos -= 1
        
        return ''.join(s_list)