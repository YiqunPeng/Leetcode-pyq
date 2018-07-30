class Solution:
    # hash table
    # time: O(n)
    # space: O(n)
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        b_dict = collections.defaultdict(list)
        for i in range(len(B)):
            b_dict[B[i]].append(i)
            
        ans = []
        for a in A:
            ans.append(b_dict[a][-1])
            b_dict[a].pop()
        return ans
    