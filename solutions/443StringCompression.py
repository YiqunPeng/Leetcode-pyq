class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        ans = 0
        pre = chars[0]
        
        cnt = 0
        for c in chars[1:]:
            if c != pre:
                if cnt > 0:
                    cnt = str(cnt + 1)
                    for i in range(len(cnt)):
                        ans += 1
                        chars[ans] = cnt[i]
                ans += 1
                chars[ans] = c
                cnt = 0
                pre = c
            else:
                cnt += 1
        
        if cnt != 0:
            cnt = str(cnt + 1)
            for i in range(len(cnt)):
                ans += 1
                chars[ans] = cnt[i]
        ans += 1
        
        return ans 
                
        