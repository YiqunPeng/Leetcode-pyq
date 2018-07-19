# from heapq import heapify, heappop, heappush

class Solution:
    # quick select: O(n) time (best case) && O(1) extra space 
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(left, right):
            pos = left
            for i in range(left, right):
                if nums[i] > nums[right]:
                    nums[i], nums[pos] = nums[pos], nums[i]
                    pos += 1
            nums[pos], nums[right] = nums[right], nums[pos]
            return pos
    
        left, right = 0, len(nums) - 1
        pos = partition(left, right)
        while left <= right:
            if k - 1 > pos:
                left = pos + 1
                pos = partition(left, right)
            elif k - 1 < pos:
                right = pos - 1
                pos = partition(left, right)
            else:
                
                return nums[pos]
        
        
    # sort: O(nlogn) time && O(1) extra space
    # def findKthLargest(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: int
    #     """
    #     return sorted(nums)[-k]
    
    # heap/priority queue: O(nlogk) time && O(k) extra space
    # def findKthLargest(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: int
    #     """
    #     heap = nums[:k]
    #     heapify(heap)
    #     for i in range(k, len(nums)):
    #         if nums[i] > heap[0]:
    #             heappush(heap, nums[i])
    #             heappop(heap)
    #     return heap[0]
        
       