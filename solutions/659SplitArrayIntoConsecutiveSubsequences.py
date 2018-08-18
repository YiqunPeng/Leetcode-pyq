class Solution:
    # hash table
    # time: O(n)
    # space: O(n)
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_dict = collections.defaultdict(int)
        for num in nums:
            num_dict[num] += 1
            
        ending_dict = collections.defaultdict(int)
        
        for num in nums:
            if num_dict[num] == 0: continue
                
            if ending_dict[num - 1] > 0:
                ending_dict[num - 1] -= 1
                ending_dict[num] += 1

                num_dict[num] -= 1
            
            elif num_dict[num + 1] > 0 and num_dict[num + 2] > 0:
                ending_dict[num + 2] += 1
                
                num_dict[num] -= 1
                num_dict[num + 1] -= 1
                num_dict[num + 2] -= 1
            
            else:
                return False
    
        return True 