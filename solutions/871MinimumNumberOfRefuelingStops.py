import queue

class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        ans = 0
        pos = startFuel
        sta_pos = 0
        pq = queue.PriorityQueue()
        while pos < target:
            while sta_pos < len(stations) and stations[sta_pos][0] <= pos:
                pq.put(-stations[sta_pos][1])
                sta_pos += 1
            if pq.empty(): return -1
            pos += -pq.get()
            ans += 1
        
        return ans