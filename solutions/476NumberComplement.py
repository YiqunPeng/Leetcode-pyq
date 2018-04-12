class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        b_num = bin(num)
        c_num = []
        for n in b_num[2:]:
            c_num.append(str(1 - int(n)))
        print(c_num)
        return int(''.join(c_num), 2)