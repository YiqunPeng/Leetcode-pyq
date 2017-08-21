class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """        
        pos, zeros = 0, 0
        while pos < len(flowerbed) and flowerbed[pos] == 0:
            zeros += 1
            pos += 1
        if pos == len(flowerbed):
            n = n - (zeros + 1) / 2
            return n <= 0
        else:
            n = n - zeros / 2
        pos, zeros = len(flowerbed) - 1, 0
        while pos >= 0 and flowerbed[pos] == 0:
            zeros += 1
            pos -= 1
        n = n - zeros / 2
        if n <= 0: return True

        zeros, cnt_flag = 0, 0 
        for i in xrange(len(flowerbed)):
            if flowerbed[i] == 1 and cnt_flag == 0:
                cnt_flag = 1
            elif flowerbed[i] == 1 and cnt_flag == 1:
                n = n - (zeros - 1) / 2
                if n <= 0: return True
                zeros= 0
            elif flowerbed[i] == 0 and cnt_flag == 1:
                zeros += 1

        return n <= 0