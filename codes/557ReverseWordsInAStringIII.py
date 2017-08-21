class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(' ')
        rev = []
        for word in words:
            rev.append(word[::-1])
        return ' '.join(rev)
