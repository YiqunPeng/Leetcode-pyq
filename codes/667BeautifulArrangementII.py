class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        ans = [1]
        l, r = 2, n
        mode = 1
        
        while k != 1:
            k -= 1
            if mode == 1:
                ans.append(r)
                r -= 1
                mode = 0
            else:
                ans.append(l)
                l += 1
                mode = 1
        
        if mode == 1:
            v = l
            for i in range(0, n-len(ans)):
                ans.append(v)
                v += 1
        else:
            v = r
            for i in range(0, n-len(ans)):
                ans.append(v)
                v -= 1
            
        return ans