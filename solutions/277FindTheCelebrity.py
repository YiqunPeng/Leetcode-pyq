# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        cele = 0
        
        for i in range(n):
            if knows(cele, i):
                cele = i
        
        for i in range(cele):
            if knows(cele, i):
                return -1
            
        for i in range(n):
            if i == cele: continue
            if not knows(i, cele):
                return -1
        
        return cele
                    
        