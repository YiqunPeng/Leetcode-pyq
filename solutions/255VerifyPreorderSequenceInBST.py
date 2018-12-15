class Solution:
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        if len(preorder) < 3: return True
        
        stack = []
        low = -sys.maxsize
        
        for i in preorder:
            if i < low: return False
            
            while stack and stack[-1] < i:
                low = stack.pop()
            stack.append(i)
            
        return True