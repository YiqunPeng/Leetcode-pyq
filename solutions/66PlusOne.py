class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[0] == 0: return [1]
        
        pos = len(digits) - 1
        digits[pos] += 1
        
        while pos > 0:
            if digits[pos] >= 10:
                digits[pos] -= 10
                digits[pos-1] += 1
            pos -= 1
                
        if digits[0] == 10:
            digits[0] -= 10
            return [1] + digits
        
        return digits