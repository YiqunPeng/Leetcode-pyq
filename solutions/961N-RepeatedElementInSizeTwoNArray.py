class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        repeats = collections.Counter(A)
        for k, v in repeats.items():
            if v == len(A) // 2: return k