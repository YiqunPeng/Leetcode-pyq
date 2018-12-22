import heapq


class ListItem:
    
    def __init__(self, row, col, val):
        self.row = row
        self.col = col
        self.val = val
     
    
    def __eq__(self, other):
        return True if self.val == other.val else False
    
    
    def __lt__(self, other):
        return True if self.val < other.val else False

    

class Solution:
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        heap = []
        
        max_val = -sys.maxsize
        for i in range(len(nums)):
            heapq.heappush(heap, ListItem(i, 0, nums[i][0]))
            max_val = max(max_val, nums[i][0])
            
        range_len = sys.maxsize
        start, end = -1, -1
        
        while len(heap) == len(nums):
            item = heapq.heappop(heap)
            r, c, v = item.row, item.col, item.val
            
            if max_val - v < range_len:
                range_len = max_val - v
                start = v
                end = max_val
                
            if c + 1 < len(nums[r]):
                heapq.heappush(heap, ListItem(r, c+1, nums[r][c+1]))
                max_val = max(max_val, nums[r][c+1])
                
        return [start, end]  