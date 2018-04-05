class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domain_dic = {}
        
        for cpdomain in cpdomains:
            [cnt, domain] = cpdomain.split(" ")
            
            domain_split = domain.split(".")
            domain_dic[domain_split[-1]] = domain_dic.get(domain_split[-1], 0) + int(cnt)
            domain_dic[domain] = domain_dic.get(domain, 0) + int(cnt)
            
            if len(domain_split) == 3:
                key = domain_split[1]+'.'+domain_split[2]
                domain_dic[key] = domain_dic.get(key, 0) + int(cnt)
        
        ans = []
        for key in domain_dic:
            ans.append(str(domain_dic[key]) + " " + key)
        return ans
            
        