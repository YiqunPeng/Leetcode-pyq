class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """        
        while len(bits) >= 2:
            if bits[0] == 0:
                bits.pop(0)
            else:
                bits.pop(0)
                bits.pop(0)
        
        if len(bits) == 1:
            return True
        else:
            return False