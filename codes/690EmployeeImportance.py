"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        ans, pos = 0, 0
        subs = []
        
        for em in employees:
            if em.id == id:
                ans += em.importance
                subs = em.subordinates
        
        while pos < len(subs):
            em = subs[pos]
            for e in employees:
                if e.id == em:
                    ans += e.importance
                    for sub in e.subordinates:
                        if sub not in subs:
                            subs.append(sub)
            pos += 1
        
        return ans