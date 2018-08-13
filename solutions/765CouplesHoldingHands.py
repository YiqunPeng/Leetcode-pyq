class Solution:
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        ans = 0
        
        pos = [0] * len(row)
        for i in range(len(row)):
            pos[row[i]] = i
            
        for i in range(0, len(row), 2):
            j = row[i] + 1 if row[i] % 2 == 0 else row[i] - 1
            if row[i+1] != j:
                row[pos[j]] = row[i+1]
                pos[row[i+1]] = pos[j]
                row[i+1] = j
                pos[j] = i + 1

                ans += 1
        
        return ans
  
