class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        dic = {}
        for c in s:
            dic[c] = dic.get(c, 0) + 1
        dic = sorted(dic.items(), key=lambda item:item[1], reverse=True)
        for key, value in dic:
            ans += (key * value)
        return ans