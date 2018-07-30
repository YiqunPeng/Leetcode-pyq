class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """  
        pos = 0
        while True:
            if pos == len(bits) - 1: 
                return True
            elif pos == len(bits) - 2 and bits[pos] == 1:
                return False
            if bits[pos] == 1:
                pos += 2
            else:
                pos += 1
