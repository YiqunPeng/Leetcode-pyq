from heapq import heapify, heappop, heappush


# heap
# time: seat(): O(logn)
#       leave(): O(n)
# space: O(n)
class Interval:
    
    def __init__(self, start, end, N):
        self.s = start
        self.e = end
        self.dis = -1
        
        if start == -1:
            self.dis = end
        elif end == N:
            self.dis = N - 1 - start
        else:
            self.dis = (end - start) // 2
            
    def __eq__(self, other):
        return self.s == other.s and self.e == other.e
    
    def __lt__(self, other):
        if self.dis != other.dis:
            return self.dis > other.dis
        else:
            return self.s < other.s
        

class ExamRoom:

    def __init__(self, N):
        """
        :type N: int
        """
        self.N = N
        self.heap = [Interval(-1, N, N)]
        heapify(self.heap)
        

    def seat(self):
        """
        :rtype: int
        """
        interval = heappop(self.heap)
        
        res = -1
        if interval.s == -1:
            res = 0
        elif interval.e == self.N:
            res = self.N - 1
        else:
            res = (interval.s + interval.e) // 2
            
        heappush(self.heap, Interval(interval.s, res, self.N))
        heappush(self.heap, Interval(res, interval.e, self.N))
            
        return res
        

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        left, right = None, None
        for interval in self.heap:
            if interval.s == p:
                right = interval
            elif interval.e == p:
                left = interval
            
            if left and right: break
                
        self.heap.remove(left)
        self.heap.remove(right)
        self.heap.append(Interval(left.s, right.e, self.N))
        
        heapify(self.heap)


# from bisect import insort

# array, binary search
# time: seat(): O(n)
#       leave(): O(n)
# space: O(n)
# class ExamRoom:

#     def __init__(self, N):
#         """
#         :type N: int
#         """
#         self.N = N
#         self.stu = []
 

#     def seat(self):
#         """
#         :rtype: int
#         """
#         if not self.stu: 
#             insort(self.stu, 0)
#             return 0
        
#         dis = self.stu[0]
#         res = 0
        
#         for i in range(len(self.stu) - 1):
#             a, b = self.stu[i], self.stu[i + 1]
            
#             if (b - a) // 2 > dis:
#                 dis = (b - a) // 2
#                 res = (b + a) // 2
                
#         if self.N - 1 - self.stu[-1] > dis:
#             res = self.N - 1
        
#         insort(self.stu, res)
#         return res
        

#     def leave(self, p):
#         """
#         :type p: int
#         :rtype: void
#         """
#         self.stu.remove(p) 
        

# # Your ExamRoom object will be instantiated and called as such:
# # obj = ExamRoom(N)
# # param_1 = obj.seat()
# # obj.leave(p)