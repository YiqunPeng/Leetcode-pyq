class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        
        while pushed:
            if stack and popped and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
                continue
            
            stack.append(pushed.pop(0))
        
        while stack and popped and stack[-1] == popped[0]:
            stack.pop()
            popped.pop(0)
         
        return len(stack) == 0