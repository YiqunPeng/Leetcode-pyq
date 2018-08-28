class Solution:
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        d = abs(target[0]) + abs(target[1])
        
        return all(d < (abs(target[0]-i) + abs(target[1]-j)) for i, j in ghosts)