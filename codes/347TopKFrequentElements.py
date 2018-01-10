class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        def shift(hp, hm):
            index = len(hp) - 1
            while index != 0:
                if hm[hp[index]] > hm[hp[index//2]]:
                    temp = hp[index//2]
                    hp[index//2] = hp[index]
                    hp[index] = temp
                    index //= 2
                else:
                    break
        
        def heap(hm):
            hp = []
            for key in hm.keys():
                hp.append(key)
                shift(hp, hm)
            return hp
        
        def top(hp, hm):
            if len(hp) == 1: return hp[0]
            val = hp[0]
            n, pos = len(hp), 0
            hp[0] = hp[n-1]
            hp.pop(-1)
            n = n - 1
            if len(hp) == 1: return val
            while pos <= (n-1) // 2:
                if 2*pos+1 < n:
                    if hm[hp[2*pos+1]]>hm[hp[2*pos]] and hm[hp[2*pos+1]]>hm[hp[pos]]:
                        temp = hp[pos]
                        hp[pos] = hp[2*pos+1]
                        hp[2*pos+1] = temp
                        pos = 2 * pos + 1
                    elif hm[hp[2*pos+1]]<=hm[hp[2*pos]] and hm[hp[2*pos]]>hm[hp[pos]]:
                        temp = hp[pos]
                        hp[pos] = hp[2*pos]
                        hp[2*pos] = temp
                        pos = 2 * pos
                    else:
                        break
                elif 2*pos < n:
                    if hm[hp[2*pos]] >= hm[hp[pos]]:
                        temp = hp[pos]
                        hp[pos] = hp[2*pos]
                        hp[2*pos] = temp
                        pos = 2 * pos
                    else:
                        break
                else:
                    break
            return val
        
        if len(nums) == 1: return [nums[0]]
        
        ans = []
        hm = {}
        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        
        hp = heap(hm)
        
        for i in range(k):
            ans.append(top(hp, hm))
            
        return ans
        