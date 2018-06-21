class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return self.dec2bin(self.bin2dec(a) + self.bin2dec(b))
    
    def dec2bin(self, a):
        if a == 0: return '0'
        bin = ''
        while a != 0:
            bin = str(a % 2) + bin
            a = a // 2
        return bin
    
    def bin2dec(self, s):
        dec = 0
        for i in range(len(s)):
            dec = dec + int(s[i]) * 2 ** (len(s) - 1 - i)
        return dec       