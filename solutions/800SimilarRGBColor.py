class Solution:
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        dic = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,
               '9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
        
        ans = '#'
        
        for i in range(3):
            tar = dic[color[1+i*2]] * 16 + dic[color[2+i*2]]
            print(tar)
            min_squ, min_val, pre_squ = sys.maxsize, -1, sys.maxsize
            for j in range(16):
                squ = (j * 17 - tar) ** 2
                if min_squ > squ:
                    min_squ = squ
                    min_val = j
                if squ > pre_squ:
                    break
                pre_squ = squ
            val_str = ''
            if min_val < 10:
                val_str = str(min_val) * 2
            else:
                val_str = chr(min_val-10+ord('a')) * 2
            ans = ans + val_str
        
        return ans