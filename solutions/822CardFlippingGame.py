class Solution:
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        same = set()
        nums = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                same.add(fronts[i])
            nums.add(fronts[i])
            nums.add(backs[i])

        nums = nums - same
        return sorted(nums)[0] if nums else 0