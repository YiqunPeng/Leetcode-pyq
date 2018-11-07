class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        count = 0
        ans = 0
        
        for s in S:
            if s == '(': count += 1
            if s == ')':
                if count > 0:
                    count -= 1
                else:
                    ans += 1
        
        return ans + count
        