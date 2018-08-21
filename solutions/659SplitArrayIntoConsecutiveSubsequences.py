class Solution:
    # greedy
    # time: O(n)
    # space: O(1)
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """  
        pre = -sys.maxsize
        p1, p2, p3 = 0, 0, 0
        
        cur, cnt = 0, 1
        c1, c2, c3 = 0, 0, 0
        
        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                cnt += 1
                continue            
            cur = nums[i]
            
            if pre + 1 != cur:
                if p1 != 0 or p2 != 0: return False    
                c1, c2, c3 = cnt, 0, 0
            else:
                if cnt < p1 + p2: return False
                c1 = max(0, cnt - p1 - p2 - p3)
                c2 = p1
                c3 = p2 + min(cnt - p1 - p2, p3)
                
            pre = cur
            p1, p2, p3 = c1, c2, c3
            cnt = 1
                
        return p1 == 0 and p2 == 0
    
    
    # hash table
    # time: O(n)
    # space: O(n)
    # def isPossible(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #     num_dict = collections.defaultdict(int)
    #     for num in nums:
    #         num_dict[num] += 1

    #     ending_dict = collections.defaultdict(int)

    #     for num in nums:
    #         if num_dict[num] == 0: continue

    #         if ending_dict[num - 1] > 0:
    #             ending_dict[num - 1] -= 1
    #             ending_dict[num] += 1

    #             num_dict[num] -= 1

    #         elif num_dict[num + 1] > 0 and num_dict[num + 2] > 0:
    #             ending_dict[num + 2] += 1

    #             num_dict[num] -= 1
    #             num_dict[num + 1] -= 1
    #             num_dict[num + 2] -= 1

    #         else:
    #             return False

    #     return True 