class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        m_list = list(magazine)
        mark = [0 for i in xrange(len(magazine))]
        for r in ransomNote:
            flag = 0
            for i in xrange(len(magazine)):
                if mark[i] == 0 and m_list[i] == r:
                    mark[i] = 1
                    flag = 1
                    break
            if flag == 0:
                return False
        return True