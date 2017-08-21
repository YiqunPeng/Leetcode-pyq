class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        ans = 0
        num = len(M)
        mark = [0 for i in xrange(num)]
        for i in xrange(num):   
            if mark[i] == 0:
                ans += 1
                friends = [i]
                friends_mark = [0 for k in xrange(num)]
                pos = 0
                while pos < len(friends):
                    for j in xrange(num):
                        if M[friends[pos]][j] == 1 and friends_mark[j] == 0:
                            friends_mark[j] = 1
                            friends.append(j)
                    pos += 1
                for k in xrange(len(friends_mark)):
                    if friends_mark[k] == 1:
                        mark[k] = 1
        return ans