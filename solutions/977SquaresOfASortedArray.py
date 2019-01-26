class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if not A: return A
        
        abs_min = abs(A[0])
        pos = 0
        for i, a in enumerate(A):
            if abs(a) <= abs_min:
                abs_min = abs(a)
                pos = i
            else:
                break

        ans = [abs_min ** 2]
        l, r = pos - 1, pos + 1
        
        while l >= 0 and r < len(A):
            if abs(A[l]) < abs(A[r]):
                ans.append(A[l] ** 2)
                l -= 1
            else:
                ans.append(A[r] ** 2)
                r += 1

        while l >= 0:
            ans.append(A[l] ** 2)
            l -= 1
        while r < len(A):
            ans.append(A[r] ** 2)
            r += 1
        
        return ans