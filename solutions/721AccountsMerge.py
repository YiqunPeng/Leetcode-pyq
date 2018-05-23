class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        father = [i for i in range(len(accounts))]
        rank = [1 for i in range(len(accounts))]
                
        def find(a):
            if father[a] == a:
                return a
            else:
                father[a] = find(father[a])
                return father[a]
                 
        def unite(a1, a2):
            f_a1, f_a2 = find(a1), find(a2)
            if f_a1 == f_a2:
                return 
            if rank[f_a1] >= rank[f_a2]:
                father[f_a2] = f_a1
                if rank[f_a1] == rank[f_a2]: rank[f_a1] += 1
            else:
                father[f_a1] = f_a2 
            
        ans = []
        
        email_to_name = {}
        for i, acc in enumerate(accounts):
            for j in acc[1:]:
                if j not in email_to_name:
                    email_to_name[j] = [i]
                else:
                    email_to_name[j].append(i)
        
        for key, value in email_to_name.items():
            if len(value) == 1: continue
            for val in value[1:]:
                unite(value[0], val)
                
        id_to_name, id_to_email = {}, {}
            
        for i in range(len(accounts)):
            if father[i] == i:
                id_to_name[i] = accounts[i][0]
            f_i = find(i)
            if f_i not in id_to_email:
                id_to_email[f_i] = accounts[i][1:]
            else:
                id_to_email[f_i].extend(accounts[i][1:])
        
        for key in id_to_name:
            emails = list(set(id_to_email[key]))
            emails.sort()
            ans.append([id_to_name[key]] + emails)
    
        return ans
            
                
                
                    
                
                