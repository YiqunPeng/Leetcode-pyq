class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five, ten = 0, 0
        
        for bill in bills:

            if bill == 5:
                five += 1
            elif bill == 10:
                if five >= 1:
                    five -= 1
                    ten += 1
                else:
                    return False
            elif bill == 20:
                if ten >= 1 and five >= 1:
                    ten -= 1
                    five -= 1
                elif ten < 1 and five >= 3:
                    five -= 3
                else:
                    return False
        
        return True