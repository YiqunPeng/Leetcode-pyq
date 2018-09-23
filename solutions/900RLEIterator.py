class RLEIterator:

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.d = {}
        self.s = [0] * (len(A) // 2)
        self.n = 0
        
        self.s[0] = A[0]
        self.d[A[0]] = A[1]
        for i in range(1, len(A) // 2):
            self.s[i] = self.s[i-1] + A[i*2]
            if A[i*2] != 0: self.d[self.s[i]] = A[i*2+1]
       
    def binary_search(self):
        if self.n > self.s[-1]: return -1
        if self.n < self.s[0]: return self.d[self.s[0]]
        
        l, r = 0, len(self.s) - 1
        while l <= r:
            m = l + (r - l) // 2
            if self.s[m] < self.n <= self.s[m+1]:
                return self.d[self.s[m+1]]
            elif self.s[m] > self.n:
                r = m - 1
            else:
                l = m + 1
        return self.d[self.s[r]]
        

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.n += n
        return self.binary_search()
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)