class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1_str, v2_str = version1.split('.'), version2.split('.')
        v1_len, v2_len = len(v1_str), len(v2_str)
        length = max(v1_len, v2_len)
        
        v1, v2 = [], []
        for i in range(length):
            if i < v1_len:
                v1.append(int(v1_str[i]))
            else:
                v1.append(0)
            if i < v2_len:
                v2.append(int(v2_str[i]))
            else:
                v2.append(0)
        
        v1_p, v2_p = 0, 0

        while v1_p < length:
            
            if v1[v1_p] < v2[v2_p]:
                return -1
            elif v1[v1_p] > v2[v2_p]:
                return 1
            else:
                if v1_p == length-1 and v2_p == length-1:
                    return 0
                elif v1_p < length and v2_p == length-1:
                    return 1
                elif v1_p == length-1 and v2_p < length:
                    return -1
                else:
                    v1_p += 1
                    v2_p += 1
        