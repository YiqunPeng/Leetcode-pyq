# from heapq import heappush, heappop, heapify

class Solution:
    # binary search
    # time: O(nlogn + nlogw) w == max(nums) - min(nums)
    # space: O(1)
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def guess(num):
            cnt = 0
            left = 0
            for right in range(len(nums)):
                while left < right and nums[right] - nums[left] > num:
                    left += 1
                cnt += right - left
            return cnt >= k
            
        
        nums.sort()
        
        low, high = 0, nums[-1] - nums[0] 
        while low < high:
            mid = low + (high - low) // 2
            if guess(mid):
                high = mid
            else:
                low = mid + 1
        
        return low
            
    
    # TLE, 16/19 cases passed
    # sort + heap
    # time: O(nlogn + nlogn + klogn)
    # space: O(n)
    # def smallestDistancePair(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: int
    #     """
    #     nums.sort()

    #     heap = []
    #     heapify(heap)
    #     for i in range(len(nums)-1):
    #         heappush(heap, (abs(nums[i]-nums[i+1]), i, i+1))

    #     while k > 1:
    #         d, i, j = heappop(heap)
    #         k -= 1
    #         if j + 1 < len(nums):
    #             heappush(heap, (abs(nums[i]-nums[j+1]), i, j+1))

    #     return heap[0][0]
        