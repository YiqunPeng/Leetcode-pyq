class Solution():
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        pos = len(digits) - 1
        digits[pos] += 1
        
        while pos > 0:
            if digits[pos] >= 10:
                digits[pos] -= 10
                digits[pos-1] += 1
            else:
                return digits
            pos -= 1
                
        if digits[0] == 10:
            digits[0] -= 10
            return [1] + digits
        
        return digits