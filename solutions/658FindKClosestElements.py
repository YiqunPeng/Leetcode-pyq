class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        pos = -1
        l, r = 0, len(arr) - 1
        while l <= r:
            m = l + (r - l) // 2
            if arr[m] == x:
                l = m
                break
            elif arr[m] < x:
                l = m + 1
            else:
                r = m - 1

        ans = []
        l, r = l - 1, l
        while k:
            if l < 0: 
                ans.append(arr[r])
                r += 1
            elif r == len(arr):
                ans.append(arr[l])
                l -= 1
            else:
                if x - arr[l] > arr[r] - x:
                    ans.append(arr[r])
                    r += 1
                else:
                    ans.append(arr[l])
                    l -= 1
            k -= 1
    
        return sorted(ans)