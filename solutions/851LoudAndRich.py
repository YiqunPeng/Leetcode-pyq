class Solution:
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        N = len(quiet)
        
        topo = [[] for i in range(N)]
        
        for richer in richer:
            x1, x2 = richer[0], richer[1]
            topo[x2].append(x1)
        
        ans = []
        for i in range(N):
            richer_list = [i]
            richer_set = set(richer_list)
            pos = 0
            min_quietness = sys.maxsize
            min_pos = -1
            while pos < len(richer_list):
                if quiet[richer_list[pos]] < min_quietness:
                    min_quietness = quiet[richer_list[pos]]
                    min_pos = richer_list[pos]
                for k in topo[richer_list[pos]]:
                    if k not in richer_set:
                        richer_set.add(k)
                        richer_list.append(k)
                pos += 1
            ans.append(min_pos)
        
        return ans