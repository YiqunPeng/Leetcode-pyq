class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        def b_search(htrs, p, l, r):
            m = (l + r) // 2
            if m == 0 and htrs[m] >= p: return 0
            if htrs[m] == p: return m
            if htrs[m] > p and htrs[m-1] < p:
                return m
            elif htrs[m] < p:
                return b_search(htrs, p, m+1, r)
            elif htrs[m-1] >= p:
                return b_search(htrs, p, l, m-1)
        
        
        # houses.sort()
        heaters.sort()
        house_num, heater_num = len(houses), len(heaters)
        
        ans = -1
        for i in range(house_num):
            pos = houses[i]
            if pos > heaters[-1]: 
                ans = max(ans, pos-heaters[-1])
                continue
                # return max(ans, max(houses-heaters[-1])
            htr_pos = b_search(heaters, pos, 0, heater_num-1)
            if htr_pos == 0:
                ans = max(ans, heaters[0]-pos)
            else:
                ans = max(ans, min(heaters[htr_pos]-pos, pos-heaters[htr_pos-1]))
        
        return ans

        