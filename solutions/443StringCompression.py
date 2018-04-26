class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if not chars: return 0
        
        pre_char = chars[0]
        cnt = 1
        ans = 0
        start, total = 0, 0
        chars_len = len(chars)
        
        while total < chars_len:
            if start+1 < len(chars) and chars[start+1] == pre_char:
                cnt += 1
                total += 1
                chars.pop(start+1)
            else:
                ans += (1 + int(math.log(cnt, 10)+1))
                total += 1
                start += 1
                if cnt != 1:
                    str_cnt = str(cnt)
                    for c in str_cnt:
                        chars.insert(start, c)
                        start += 1
                cnt = 1
                if start < len(chars):
                    pre_char = chars[start]                        
        
        ans = ans + 1 + int(math.log(cnt, 10)+1)
        print(ans)