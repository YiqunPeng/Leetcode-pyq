class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        def range_sum(i, j):
            return read(j) - read(i-1)
        
        def update(idx, val):
            while idx <= len(flowers):
                bit[idx] += val
                idx += (idx & -idx)
        
        def read(idx):
            res = 0
            while idx > 0:
                res += bit[idx]
                idx -= (idx & -idx)
            return res
        
        
        N = len(flowers)
        bit = [0] * (N + 1)
        bloomed = set()
        
        for i in range(N):
            idx = flowers[i]
            bloomed.add(idx)
            if idx - k - 1 in bloomed and range_sum(idx-k, idx-1) == 0:
                return i + 1
            elif idx + k + 1 in bloomed and range_sum(idx+1, idx+k) == 0:
                return i + 1
            update(idx, 1)
        
        return -1
