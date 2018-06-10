from bisect import bisect_left, insort_left

class Solution:
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        window = nums[:k]
        window.sort()
        ans = []

        is_odd = True if k % 2 == 1 else False

        for i in range(k, len(nums)):
            if is_odd:
                ans.append(window[k//2] / 1.)
            else:
                ans.append((window[k//2-1] + window[k//2]) / 2.)
            window.pop(bisect_left(window, nums[i-k]))
            insort_left(window, nums[i])
        if is_odd:
            ans.append(window[k//2] / 1.)
        else:
            ans.append((window[k//2-1] + window[k//2]) / 2.)
        return ans
    
#     def medianSlidingWindow(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[float]
#         """
#         def binary_search_eq(w, l, r, tar):
#             mid = l + (r - l) // 2
#             if w[mid] == tar:
#                 return mid
#             elif w[mid] < tar:
#                 return binary_search_eq(w, mid+1, r, tar)
#             else:
#                 return binary_search_eq(w, l, mid-1, tar)
            
#         def binary_search_gtr(w, l, r, tar):
#             mid = l + (r - l) // 2
#             if w[mid] <= tar and w[mid+1] >= tar:
#                 return mid
#             elif w[mid+1] <= tar:
#                 return binary_search_gtr(w, mid+1, r, tar)
#             elif w[mid] > tar:
#                 return binary_search_gtr(w, l, mid-1, tar)
            
#         window = nums[0:k]
#         window.sort()
        
#         if k % 2 == 1:
#             med = float(window[k//2])
#         else:
#             med = (window[k//2] + window[k//2-1]) / 2.
#         ans = [med]
        
#         for i in range(k, len(nums)):
#             pre = binary_search_eq(window, 0, k-1, nums[i-k])
#             window = window[:pre] + window[pre+1:]
#             if not window:
#                 window = [nums[i]]    
#             elif nums[i] <= window[0]:
#                 window = [nums[i]] + window
#             elif nums[i] >= window[-1]:
#                 window = window + [nums[i]]
#             else:
#                 post = binary_search_gtr(window, 0, k-2, nums[i])
#                 window = window[:post+1] + [nums[i]] + window[post+1:]
#             if k % 2 == 1:
#                 med = window[k//2] / 1.
#             else:
#                 med = (window[k//2] + window[k//2-1]) / 2.
#             ans.append(med)
        
#         return ans
                
                    
        