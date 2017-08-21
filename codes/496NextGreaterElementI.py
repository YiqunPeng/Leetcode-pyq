class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        
        len1 = len(findNums)
        len2 = len(nums)
        
        for num in findNums:
            res.append(self.find_gtr_ele(num, nums))
            
        return res
    
    def find_gtr_ele(self, num, nums):
        flag = 0
        for n in nums:
            if n == num:
                flag = 1
            if flag == 1 and n > num:
                return n
        return -1