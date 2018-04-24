class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total = 0
        sum = 0
        pos = 0
        
        for i in range(len(gas)):
            sum = sum + gas[i] - cost[i]
            total = total + gas[i] - cost[i]
            if sum < 0:
                sum = 0
                pos = i + 1
        
        return pos if total >= 0 else -1
                
        
        
        
        