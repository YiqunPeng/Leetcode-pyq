class Solution:
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        m = 10 ** 9 + 7
        ans = 0
        
        right = [0] * len(A)
        left = [0] * len(A)
        
        stack = [0]
        for i in range(1, len(A)):
            if A[i] <= A[stack[-1]]:
                while stack and A[i] <= A[stack[-1]]:
                    right[stack[-1]] = i - stack[-1]
                    stack.pop()
            stack.append(i)

        for i in range(len(stack)):
            right[stack[i]] = len(A) - stack[i]
            
        stack = [len(A)-1]
        for i in range(len(A)-2, -1, -1):
            if A[i] < A[stack[-1]]:
                while stack and A[i] < A[stack[-1]]:
                    left[stack[-1]] = stack[-1] - i
                    stack.pop()
            stack.append(i)
        for i in range(len(stack)):
            left[stack[i]] = stack[i] + 1

        for i in range(len(right)):
            ans = ans + (right[i] * left[i] * A[i]) % m
        return ans % m