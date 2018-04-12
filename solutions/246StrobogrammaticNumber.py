class Solution:
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dic = {'0': '0', '1': '1', '6' : '9', '8': '8', '9': '6'}
        
        left, right = 0, len(num) - 1
        
        while left <= right:
            if num[left] not in dic or num[right] not in dic or dic[num[right]] != num[left]:
                return False
            else:
                left += 1
                right -= 1
        
        return True