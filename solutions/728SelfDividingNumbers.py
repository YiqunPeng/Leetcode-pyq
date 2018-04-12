class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def self_dividing(n):
            num = n
            while n != 0:
                r = n % 10
                if r == 0: return False
                if num % r != 0:
                    return False
                n //= 10             
            return True            
        
        ans = []
        
        for num in range(left, right+1):
            if self_dividing(num):
                ans.append(num)
                
        return ans