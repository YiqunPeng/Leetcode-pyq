class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1: return 1
        if n==2: return 2
        
        one_step, two_step, min_list = [], [], []
        ann_dict = {}
        
        for i in xrange(0, n/2+1):
            two_step.append(i)
            one_step.append(n - i * 2)
            min_list.append(min(two_step[i], one_step[i]))
        ann_dict[0] = 1
        for i in xrange(1, max(min_list)+1):
            ann_dict[i] = i * ann_dict.get(i-1, 1)
        
        ans = 0
        for i in xrange(0, n/2+1):
            m = two_step[i]
            n = one_step[i]
            temp = 1
            if n > m:
                for j in xrange(n+1, n+m+1):
                    temp *= j
                temp = temp / ann_dict[m]
            else:
                for j in xrange(m+1, n+m+1):
                    temp *= j
                temp = temp / ann_dict[n]
            print(temp)
            ans += temp
        
        return ans