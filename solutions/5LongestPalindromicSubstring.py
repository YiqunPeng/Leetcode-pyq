class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def palind_string(s, left, right, s_len):
            while left >= 1 and right < s_len-1:
                if s[left-1] == s[right+1]:
                    left -= 1
                    right += 1
                else:
                    break
            return [left, right]
        
        
        if not s: return ''
        
        s_len = len(s)
        left, right = 0, 0
        
        order = []
        if s_len % 2 == 0:
            order.append(s_len//2)
            order.append(s_len//2-1)
            l = s_len // 2 - 2
            r = s_len // 2 + 1
            while l >= 0:
                order.append(l)
                order.append(r)
                l -= 1
                r += 1
        else:
            order.append((s_len-1)//2)
            l = (s_len - 1) // 2 - 1
            r = (s_len - 1) // 2 + 1
            while l >= 0:
                order.append(l)
                order.append(r)
                l -= 1
                r += 1
        
        for i in order:
            if (i+1)*2 < (right-left+1):
                break
            if i < s_len - 1 and s[i] == s[i+1]:
                [l, r] = palind_string(s, i, i+1, s_len)
                if r - l > right - left:
                    left, right = l, r
            if i > 0 and i < s_len - 1 and s[i-1] == s[i+1]:
                [l, r] = palind_string(s, i-1, i+1, s_len)
                if r - l > right - left:
                    left, right = l, r

        return s[left:right+1]