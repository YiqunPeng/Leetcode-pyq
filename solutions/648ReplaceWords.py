class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        index = [[] for i in xrange(26)]
        dict.sort()
        for root in dict:
            index[ord(root[0])-ord('a')].append(root)
        words = sentence.split(' ')
        for i in xrange(len(words)):
            for root in index[ord(words[i][0])-ord('a')]:
                if words[i].startswith(root):
                    words[i] = root
                    break
        return ' '.join(words)