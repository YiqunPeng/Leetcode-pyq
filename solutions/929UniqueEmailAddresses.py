class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        d = collections.defaultdict(set)
        
        for email in emails:
            parts = email.split('@')
            local, domain = parts[0], parts[1]
            
            s = ''
            for c in local:
                if c == '+': break
                if c == '.': continue
                s += c
            
            d[domain].add(s)
        
        ans = 0
        for k, v in d.items():
            ans += len(v)
        return ans