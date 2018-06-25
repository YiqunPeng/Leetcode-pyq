class Solution:
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        pre = [0] * n
        pre[0] = nums[0]
        for pos in range(1, n):
            pre[pos] = pre[pos-1] + nums[pos]
        # print(pre)
        
        for i in range(1, n-5):
            left = pre[i-1]
            for k in range(n-2, i+3, -1):
                right = pre[-1] - pre[k]
                if left == right:
                    for j in range(i+2, k-1):
                        ij, jk = pre[j-1] - pre[i], pre[k-1] - pre[j]
                        if ij == jk and ij == right:
                            return True
        
        return False
                        