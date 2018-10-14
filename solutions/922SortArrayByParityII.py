class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd, even = [], []
        for a in A:
            if a % 2 == 0:
                even.append(a)
            else:
                odd.append(a)
        
        ans = []
        po, pe = 0, 0
        for i in range(len(A)):
            if i % 2 == 0:
                ans.append(even[pe])
                pe += 1
            else:
                ans.append(odd[po])
                po += 1
        return ans