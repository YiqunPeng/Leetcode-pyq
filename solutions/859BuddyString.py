class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B): return False
        if len(A) < 2: return False
        
        same = False
        dic = {}
        pos = []
        
        for i in range(len(A)):
            if A[i] in dic:
                same = True
            else:
                dic[A[i]] = 0
            if A[i] != B[i]:
                pos.append(i)
                if len(pos) > 2: return False
        
        if len(pos) == 0 and same:
            return True
        if len(pos) != 2:
            return False
        if A[pos[0]] == B[pos[1]] and B[pos[0]] == A[pos[1]]:
            return True
        else:
            return False