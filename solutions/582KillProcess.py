class Solution:
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        p_dic = {}
        for i in range(len(ppid)):
            if ppid[i] in p_dic:
                p_dic[ppid[i]].append(pid[i])
            else:
                p_dic[ppid[i]] = [pid[i]]
        
        ans = []
        q = [kill]
        
        while q:
            p = q.pop()
            ans.append(p)
            if p in p_dic:
                q = q + p_dic[p]
        
        return ans