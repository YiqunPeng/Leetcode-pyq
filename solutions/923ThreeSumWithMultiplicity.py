class Solution:
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        mod = 10 ** 9 + 7
        a_dict = collections.Counter(A)
        
        ans = 0
        
        for i, j in itertools.combinations_with_replacement(a_dict, 2):
            k = target - i - j
            vi, vj, vk = a_dict[i], a_dict[j], a_dict[k]
            if i == j == k:
                ans = (ans + (vi * (vi - 1) * (vi - 2) // 6) % mod) % mod
            elif i == j != k:
                ans = (ans + (vi * (vi - 1) // 2 * vk) % mod) % mod
            elif i < k and j < k:
                ans = (ans + vi * vj * vk % mod) % mod
        
        return ans      