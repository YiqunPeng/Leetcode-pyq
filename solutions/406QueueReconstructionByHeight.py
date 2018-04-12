class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        if not people: return ans
        people = sorted(people, key=lambda x:x[1])
        for p in people:
            cnt, index = 0, 0
            for i in xrange(len(ans)):
                if ans[i][0] >= p[0]:
                    cnt += 1
                if cnt > p[1]:
                    index = i
                    break
            if cnt <= p[1]:
                ans.append(p)
            else:
                ans.insert(index, p)
        return ans
        