class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return self.binary_search(num, 1, num)
    
    def binary_search(self, num, l, r):
        if l > r:
            return False
        mid = (l + r) / 2
        if mid ** 2 == num:
            return True
        elif mid ** 2 > num:
            return self.binary_search(num, l, mid-1)
        else:
            return self.binary_search(num, mid+1, r)