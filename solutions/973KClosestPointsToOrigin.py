import heapq


class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        heap = []
        
        for x, y in points:
            dis = x ** 2 + y ** 2            
            heapq.heappush(heap, (-dis, x, y))
            if len(heap) > K:
                heapq.heappop(heap)
                
        ans = []
        while heap:
            dis, x, y = heapq.heappop(heap)
            ans.append([x, y])
            
        return ans