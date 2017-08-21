class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ans = ''
        
        for i in xrange(int(math.ceil(len(s)/(2*k)))):
            k_list = list(s[2*k*i:(2*k*i+k)])
            k_list.reverse()
            ans = ans + ''.join(k_list) + s[(2*k*i+k):(2*k*(i+1))]
            
        i = int(math.ceil(len(s)/(2*k)))
        if (len(s) - 2 * i * k) < k:
            k_list = list(s[(2*k*i):])
            k_list.reverse()
            ans = ans + ''.join(k_list)
        else:
            k_list = list(s[(2*k*i):(2*k*i+k)])
            k_list.reverse()
            ans = ans + ''.join(k_list) + s[(2*k*i+k):]
        
        return ans