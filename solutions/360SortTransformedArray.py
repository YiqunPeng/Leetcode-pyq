class Solution:
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        n = len(nums)
        ans = [0] * n
        
        if a == 0:
            if b == 0:
                return [c] * n
            elif b > 0:
                return [b * i + c for i in nums]
            else:
                return [b * i + c for i in nums][::-1]
        else:
            m = - b / (2 * a) / 1.
            pos, dis = 0, sys.maxsize
            for i in range(n):
                if abs(nums[i] - m) < dis:
                    dis = abs(nums[i] - m)
                    pos = i
            ans[0] = a * nums[pos] ** 2 + b * nums[pos] + c
            left, right = pos - 1, pos + 1
            pos = 1
            while left >= 0 and right < n:
                if abs(nums[left] - m) > abs(nums[right] - m):
                    ans[pos] = a * nums[right] ** 2 + b * nums[right] + c
                    right += 1
                    pos += 1
                else:
                    ans[pos] = a * nums[left] ** 2 + b * nums[left] + c
                    left -= 1
                    pos += 1
            if left >= 0:
                for i in range(left, -1, -1):
                    ans[pos] = a * nums[i] ** 2 + b * nums[i] + c
                    pos += 1
            elif right < n:
                for i in range(right, n):
                    ans[pos] = a * nums[i] ** 2 + b * nums[i] + c
                    pos += 1
        
        return ans if a > 0 else ans[::-1]
        
