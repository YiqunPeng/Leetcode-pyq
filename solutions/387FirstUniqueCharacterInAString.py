class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        c_hash = [0 for i in xrange(26)]
        c_list = list(s)
        for c in c_list:
            c_hash[ord(c) - ord('a')] += 1
        for i in xrange(len(c_list)):
            if c_hash[ord(c_list[i]) - ord('a')] == 1:
                return i
        return -1
            