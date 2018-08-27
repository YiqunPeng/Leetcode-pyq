class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        group = set()
        
        for a in A:
            e, o = set(), set()
            
            for i in range(len(a)):
                if i % 2 == 0:
                    e.add(a[i])
                else:
                    o.add(a[i])
            
            if (str(sorted(list(e))), str(sorted(list(o)))) not in group:
                group.add((str(sorted(list(e))), str(sorted(list(o)))))
        
        return len(group)