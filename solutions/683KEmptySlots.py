class Solution:
    # array
    # time: O(n)
    # space: O(n)
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        length = len(flowers)
        days = [0] * length
        for i, f in enumerate(flowers):
            days[f-1] = i + 1

        left, right = 0, k + 1
        ans = sys.maxsize
        pos = 1
        while right < length:
            if pos == right or days[pos] < max(days[left], days[right]):
                if pos == right: ans = min(ans, max(days[left], days[right]))
                left = pos
                right = left + k + 1
            pos += 1

        return ans if ans != sys.maxsize else -1
    
    
    # binary index tree
    # time: O(nlogn)
    # space: O(n)
    # def kEmptySlots(self, flowers, k):
    #     """
    #     :type flowers: List[int]
    #     :type k: int
    #     :rtype: int
    #     """
    #     def get_range_sum(i, j):
    #         return read(j) - read(i-1)

    #     def update(idx, val):
    #         while idx < len(tree):
    #             tree[idx] += val
    #             idx += (idx & -idx)

    #     def read(idx):
    #         res = 0
    #         while idx > 0:
    #             res += tree[idx]
    #             idx -= (idx & -idx)
    #         return res


    #     tree = [0] * (len(flowers) + 1)
    #     bloomed = set()

    #     for i in range(len(flowers)):
    #         update(flowers[i], 1)
    #         bloomed.add(flowers[i])
    #         if flowers[i] + k + 1 in bloomed and get_range_sum(flowers[i]+1, flowers[i]+k) == 0:
    #             return i + 1
    #         if flowers[i] - k - 1 in bloomed and get_range_sum(flowers[i]-k, flowers[i]-1) == 0:
    #             return i + 1

    #     return -1
           