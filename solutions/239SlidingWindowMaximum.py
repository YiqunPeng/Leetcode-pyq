# import heapq


class Solution:
    # deque
    # time: O(n)
    # space: O(k)
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums: return []

        dq = collections.deque()
        ans = []

        for i in range(len(nums)):
            if i < k - 1:
                while dq and dq[-1] < nums[i]:
                    dq.pop()
                dq.append(nums[i])
            else:
                if dq and nums[i-k] == dq[0]:
                    dq.popleft()
                while dq and dq[-1] < nums[i]:
                    dq.pop()
                dq.append(nums[i])
                ans.append(dq[0])

        return ans  
    
    
    # heap
    # time: O(nlogn)
    # space: O(k)
    # def maxSlidingWindow(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: List[int]
    #     """
    #     if not nums: return []

    #     heap = []
    #     ans = []

    #     for i in range(len(nums)):
    #         if i < k:
    #             heapq.heappush(heap, -nums[i])
    #             if i == k - 1: ans.append(-heap[0])
    #         else:
    #             heap.remove(-nums[i-k])
    #             heapq.heapify(heap)
    #             heapq.heappush(heap, -nums[i])
    #             ans.append(-heap[0])

    #     return ans