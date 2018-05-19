class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        t_num, t_i = [0] * 26, [0] * 26
        for t in tasks:
            t_num[ord(t)-ord('A')] += 1
        t_index = []
        for i in range(26):
            if t_num[i] > 0:
                t_index.append(i)
        
        ans = 0
        
        while 1:
            done_flag = True
            max_num = 0
            task = -1
            for i in t_index:
                if t_i[i] == 0 and t_num[i] > max_num:
                    max_num = t_num[i]
                    task = i
                if t_num[i] != 0:
                    done_flag = False
                if t_i[i] > 0:
                    t_i[i] -= 1
            if done_flag:
                return ans
            if task != -1:
                t_num[task] -= 1
                t_i[task] = n
            ans += 1
        
        return ans
                
        
        
        