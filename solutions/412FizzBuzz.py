class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        
        for i in range(1, n+1):
            if i % 15 == 0:
                res.append('FizzBuzz')
                continue
            if i % 3 == 0:
                res.append('Fizz')
                continue
            if i % 5 == 0:
                res.append('Buzz')
                continue
            res.append(str(i))
        
        return res