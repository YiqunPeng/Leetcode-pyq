class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        ans = []
        
        a = A.split(' ')
        b = B.split(' ')
        
        a_dict = collections.defaultdict(int)
        for i in a:
            a_dict[i] += 1
        b_dict = collections.defaultdict(int)
        for i in b:
            b_dict[i] += 1
            
        for k in a_dict.keys():
            if a_dict[k] == 1 and b_dict[k] == 0:
                ans.append(k)
        for k in b_dict.keys():
            if b_dict[k] == 1 and a_dict[k] == 0:
                ans.append(k)
        
        return ans