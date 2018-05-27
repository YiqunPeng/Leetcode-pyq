class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        N = len(rooms)        
        v = [0] * N
        v[0] = 1
        
        q = rooms[0]
        while q:
            key = q.pop(0)
            if v[key] == 1:
                continue
            else:
                q.extend(rooms[key])
                v[key] = 1
        
        return sum(v) == N
        
        