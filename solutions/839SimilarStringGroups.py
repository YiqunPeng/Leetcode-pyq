class Solution:
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        def similiar(s1, s2):
            cnt = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]: cnt += 1
                if cnt > 2: return False
            return cnt == 2
        
        def find(s):
            if father[s] != s: father[s] = find(father[s])
            return father[s]

        A = list(set(A))
        father = {a: a for a in A}
        n, m = len(A), len(A[0])
        
        ans = n
        
        if n < m:
            for i in range(len(A)):
                for j in range(i+1, len(A)):
                    fs1, fs2 = find(A[i]), find(A[j])
                    if similiar(A[i], A[j]) and fs1 != fs2:
                        father[fs2] = fs1
                        ans -= 1
        else:
            for a in A:
                for i in range(len(a)):
                    for j in range(i+1, len(a)):
                        if a[i] == a[j]: continue
                        n_a = a[:i] + a[j] + a[i+1:j] + a[i] + a[j+1:]
                        if n_a in father:
                            fs1, fs2 = find(a), find(n_a)
                            if fs1 != fs2:
                                father[fs2] = fs1
                                ans -= 1
        
        return ans