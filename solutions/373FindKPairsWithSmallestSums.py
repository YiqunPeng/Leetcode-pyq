import heapq

class Solution:
    # heap
    # time: O(klogk)
    # space: O(klogk)
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2 or k == 0: return []
        
        heap = [(nums1[0]+nums2[0], 0, 0)]
        heapq.heapify(heap)
        
        pair_set = set()
        pair_set.add((0, 0))
        
        ans = []
        while heap and k > 0:
            s, i1, i2 = heapq.heappop(heap)
            ans.append([nums1[i1], nums2[i2]])
            k -= 1
            if i2 + 1 < len(nums2) and (i1, i2+1) not in pair_set:
                heapq.heappush(heap, (nums1[i1]+nums2[i2+1], i1, i2+1))
                pair_set.add((i1, i2+1))
            if i1 + 1 < len(nums1) and (i1+1, i2) not in pair_set:
                heapq.heappush(heap, (nums1[i1+1]+nums2[i2], i1+1, i2))
                pair_set.add((i1+1, i2))
        
        return ans