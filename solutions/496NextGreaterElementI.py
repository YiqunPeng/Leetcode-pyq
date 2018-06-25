class Solution():
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        dic = {}
        for num in nums:
            while stack and stack[-1] < num:
                dic[stack.pop()] = num
            stack.append(num)
        
        for i in range(len(findNums)):
            findNums[i] = dic.get(findNums[i], -1)
        return findNums