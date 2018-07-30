import bisect

class Solution:
    # two pointer
    # time: O(n + m)
    # space: O(1)
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s: return True

        s_p, t_p = 0, 0
        s_len, t_len = len(s), len(t)

        while s_p < s_len and t_p < t_len:
            if s[s_p] == t[t_p]:
                s_p += 1
                t_p += 1
            else:
                t_p += 1

        return True if s_p == s_len else False
    
    
    # for follow-up
    # binary search
    # time: O(n + kmlogn) n == len(t), k == number of string s, m == len(s)
    # def isSubsequence(self, s, t):
    #     """
    #     :type s: str
    #     :type t: str
    #     :rtype: bool
    #     """
    #     t_dict = collections.defaultdict(list)
    #     for i in range(len(t)):
    #         t_dict[t[i]].append(i)

    #     pre = 0
    #     for c in s:
    #         if c not in t_dict: return False
    #         idx = bisect.bisect_left(t_dict[c], pre)
    #         if idx == len(t_dict[c]): return False
    #         pre = t_dict[c][idx] + 1

    #     return True
