class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def is_palindromic(string):
            ori = list(string)
            rev = [item for item in ori]
            rev.reverse()
            return True if ori == rev else False
        
        cnt = [0] * len(s)
        mark = [[0]*len(s) for i in xrange(len(s))]
        for i in xrange(1, len(s)):
            for j in xrange(i):
                if s[j] == s[i]:
                    if mark[j+1][i-1] == 1:
                        cnt[i] += 1
                        mark[j][i] = 1
                    elif mark[j+1][i-1] == -1:
                        mark[j][i] = -1
                    else:
                        if is_palindromic(s[j+1:i]):
                            mark[j+1][i-1] = 1
                            mark[j][i] = 1
                            cnt[i] += 1
                        else:
                            mark[j+1][i-1] = -1
                            mark[j][i] = -1
                else:
                    mark[j][i] = -1
            cnt[i] += cnt[i-1]
        return cnt[len(s)-1] + len(s)
                    