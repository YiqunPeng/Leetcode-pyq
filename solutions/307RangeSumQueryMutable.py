class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        self.bit = [0] * (self.n + 1)
        for i in range(self.n):
            self.update(i, nums[i])
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """        
        val -= self.read(i+1) - self.read(i)
        i += 1
        while i <= self.n:
            self.bit[i] += val
            i += (i & -i)
    
    
    def read(self, idx):
        res = 0
        while idx > 0:
            res += self.bit[idx]
            idx -= (idx & -idx)
        return res
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.read(j+1) - self.read(i)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
