from queue import Queue

class Solution:
    # queue, iterative
    # time: O(4^n)
    # space: O(4^n)
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans = []
        d_len = len(digits)
        if not digits or '0' in digits or '1' in digits: return ans
        
        mappings = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'],
                    ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

        q = Queue()
        for i in mappings[int(digits[0])]:
            q.put((i, 1))
        
        while not q.empty():
            s, l = q.get()
            if l == d_len: 
                ans.append(s)
            else:
                for i in mappings[int(digits[l])]:
                    q.put((s+i, l+1))
        
        return ans
        
        
    # dfs/backtracking 
    # time: O(4^n)
    # space: O(1)
    # def letterCombinations(self, digits):
    #     """
    #     :type digits: str
    #     :rtype: List[str]
    #     """
    #     def dfs(index, d_len, s):
    #         if index == d_len:
    #             ans.append(s)
    #             return
    #         for l in mappings[int(digits[index])]:
    #             dfs(index+1, d_len, s+l)

    #     if not digits or '0' in digits or '1' in digits: return [] 
    #     ans = []
    #     mappings = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'],
    #                 ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

    #     dfs(0, len(digits), '')
    #     return ans
        