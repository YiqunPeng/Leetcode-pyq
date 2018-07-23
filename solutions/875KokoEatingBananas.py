class Solution:
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        def can_finish(speed):
            cnt = 0
            for p in piles:
                if p % speed == 0:
                    cnt += p // speed
                else:
                    cnt += p // speed + 1
            return cnt <= H
        
        n = len(piles)
        max_p = max(piles)
        if n == H: return max_p
        
        left, right = 1, max_p
        while left <= right:
            mid = left + (right-left) // 2
            can_mid = can_finish(mid)
            can_mid_1 = can_finish(mid-1) if mid > 1 else False
            if can_mid and not can_mid_1:
                return mid
            if can_mid and can_mid_1:
                right = mid - 1
            elif not can_mid:
                left = mid + 1