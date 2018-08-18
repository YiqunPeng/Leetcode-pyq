class Solution:
    # bucket sort
    # time: O(n)
    # space: O(n)
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = collections.defaultdict(int)
        for num in nums:
            freq[num] += 1
            
        bucket = [[] for i in range(len(nums)+1)]
        for key in freq:
            bucket[freq[key]].append(key)
         
        ans = []
        pos = len(bucket) - 1
        while k:
            if bucket[pos]:
                for key in bucket[pos]:
                    ans.append(key)
                    k -= 1
                    if k == 0: return ans
            pos -= 1
        
        return ans