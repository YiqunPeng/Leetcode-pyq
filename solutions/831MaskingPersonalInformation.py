class Solution:
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        def mask_email(s):
            s = s.lower()
            splits = s.split('@')
            name = splits[0]
            return name[0] + '*' * 5 + name[-1] + '@' + splits[1]
        
        def mask_phone(s):
            p_s = ''
            for c in s:
                if c in string.digits:
                    p_s += c
            res = ''
            if len(p_s) == 10:
                res = '***-***-' + p_s[-4:]
            else:
                res = '+' + '*' * (len(p_s) - 10) + '-***-***-' + p_s[-4:]
            return res
                   
        
        if '@' in S:
            return mask_email(S)
        else:
            return mask_phone(S)
        