class Solution:
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        a_dict = {}
        b_dict = collections.defaultdict(int)
        
        for b in B:
            temp = collections.defaultdict(int)
            for c in b:
                temp[c] += 1
            for k, v in temp.items():
                if v > b_dict[k]:
                    b_dict[k] = v

        ans = []
        for a in A:
            temp = collections.defaultdict(int)
            for c in a:
                temp[c] += 1
            if all(b_dict[k] <= temp[k] for k, v in b_dict.items()):
                ans.append(a)
        
        return ans