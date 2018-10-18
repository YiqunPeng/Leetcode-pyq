import bisect

class Solution:
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        if not nums: return []
        
        odd = k % 2 
        
        win = sorted(nums[:k])
        ans = []
        if odd:
            ans.append(win[k // 2] / 1.)
        else:
            ans.append((win[k // 2] + win[k // 2 - 1]) / 2.)
        
        for i in range(k, len(nums)):          
            win.pop(bisect.bisect_left(win, nums[i-k]))
            bisect.insort_left(win, nums[i])
            if odd:
                ans.append(win[k // 2] / 1.)
            else:
                ans.append((win[k // 2] + win[k // 2 - 1]) / 2.) 
        
        return ans                   