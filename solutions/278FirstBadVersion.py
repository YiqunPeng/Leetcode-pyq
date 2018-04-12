# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = (left + right) / 2
            cur_version = isBadVersion(mid)
            pre_version = isBadVersion(mid - 1)
            if cur_version and not pre_version:
                return mid
            if cur_version:
                right = mid - 1
            else:
                left = mid + 1