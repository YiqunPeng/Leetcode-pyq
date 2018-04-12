class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m+n-1, -1, -1):
            if n == 0:
                nums1[i] = nums1[m-1]
                m -= 1
                continue
            if m == 0:
                nums1[i] = nums2[n-1]
                n -= 1
                continue
            if nums1[m-1] > nums2[n-1]:
                nums1[i] = nums1[m-1]
                m -= 1
            else:
                nums1[i] = nums2[n-1]
                n -= 1
        