class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_int = [int(i) for i in str(num)]
        
        for pos in range(0, len(num_int)):
            max_num = num_int[pos]
            for i in range(pos+1, len(num_int)):
                max_num = max(max_num, num_int[i])
                            
            if max_num == num_int[pos]:
                continue
        
            for i in range(len(num_int)-1, pos, -1):
                if num_int[i] == max_num:
                    temp = num_int[i]
                    num_int[i] = num_int[pos]
                    num_int[pos] = temp
                    num_str = [str(j) for j in num_int]
                    return int(''.join(num_str))
                
        return num
        