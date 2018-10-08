class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = [''] * n
        
        for i in range(1, n + 1):
            if i % 15 == 0:
                ans[i - 1] = 'FizzBuzz'
            elif i % 3 == 0:
                ans[i - 1] = 'Fizz'
            elif i % 5 == 0:
                ans[i - 1] = 'Buzz'
            else:
                ans[i - 1] = str(i)
        
        return ans    