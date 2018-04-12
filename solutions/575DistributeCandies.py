class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        cnt = len(set(candies))
        if cnt > len(candies)//2:
            return len(candies)//2
        else:
            return cnt