class Solution:
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        binary = []
        for d in data:
            b = bin(d)[2:]
            if len(b) > 8: b = b[-8:]
            if len(b) < 8: b = '0' * (8 - len(b)) + b       
            binary.append(b)
        
        pos = 0
        while pos < len(binary):
            if binary[pos][0] == '0':
                pos += 1
                continue
            else:
                cnt = 0
                for i in binary[pos]:
                    if i == '1':
                        cnt += 1
                    else:
                        break
                
                if cnt == 1 or cnt > 4 or pos + cnt - 1 >= len(binary): return False
                for i in range(1, cnt):
                    if binary[pos+i][0:2] != '10': return False
                
                pos += cnt
                
        return True