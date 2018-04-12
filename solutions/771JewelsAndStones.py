class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        hash_map = [0] * 52
        for j in J:
            if j >= 'a' and j <= 'z':
                hash_map[ord(j)-ord('a')] = 1
            else:
                hash_map[ord(j)-ord('A')+26] = 1
        
        ans = 0
        
        for s in S:
            if s >= 'a' and s <= 'z':
                if hash_map[ord(s)-ord('a')] == 1:
                    ans += 1
            else:
                if hash_map[ord(s)-ord('A')+26] == 1:
                    ans += 1
        
        return ans
        