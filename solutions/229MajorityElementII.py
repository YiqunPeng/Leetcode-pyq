class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num1, cnt1 = 0, 0
        num2, cnt2 = 1, 0
        
        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1
            else:
                if cnt1 == 0:
                    num1, cnt1 = num, 1
                elif cnt2 == 0:
                    num2, cnt2 = num, 1
                else:
                    cnt1, cnt2 = cnt1 - 1, cnt2 - 1
        
        return [num for num in (num1, num2) if nums.count(num) > len(nums) // 3]
        
        
