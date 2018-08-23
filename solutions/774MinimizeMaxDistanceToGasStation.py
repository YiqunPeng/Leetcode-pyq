class Solution:
    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        def add_station(dis):
            cnt = 0
            for i in range(1, len(stations)):
                if (stations[i]-stations[i-1]) % dis == 0:
                    cnt += (stations[i]-stations[i-1]) // dis - 1
                else:
                    cnt += (stations[i]-stations[i-1]) // dis
                if cnt > K: return -1
            return 1
        
        curr_max = -1
        for i in range(1, len(stations)):
            curr_max = max(curr_max, stations[i] - stations[i-1])
            
        min_diff = 1e-6

        left, right = 0., curr_max * 1.
        while left + min_diff < right:
            mid = left + (right - left) / 2.
            if mid == right:
                return mid
            k = add_station(mid)
            if k == -1:
                left = mid 
            else:
                right = mid
        
        return right
