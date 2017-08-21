class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0: return False
        
        div_list = [1]
        for i in xrange(2, int(math.sqrt(num))+1):
            if num % i == 0:
                div_list.append(i)
                div_list.append(num/i)
        if int(math.sqrt(num)) ** 2 == num:          
            return sum(div_list)-math.sqrt(num) == num
        else:
            return sum(div_list) == num
            