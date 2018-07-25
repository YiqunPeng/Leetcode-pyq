class Solution:
    # string
    # time: O(n^2) n -- len(time)
    # space: O(n) or O(1)
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        hour = int(time[:2])
        minute = int(time[3:])
        nums = [int(time[0]), int(time[1]), int(time[3]), int(time[4])]

        nxt_h, nxt_m = 99, 99
        min_v = 99

        for i in range(4):
            for j in range(4):
                a = nums[i] * 10 + nums[j]
                min_v = min(min_v, a)
                if minute < a <= 59:
                    nxt_m = min(nxt_m, a)
                if hour < a <= 23:
                    nxt_h = min(nxt_h, a)

        min_v = '0' * (2 - len(str(min_v))) + str(min_v) 

        if 59 >= nxt_m > minute:
            nxt_m = '0' * (2 - len(str(nxt_m))) + str(nxt_m)
            return time[:3] + nxt_m
        elif 23 >= nxt_h > hour:
            nxt_h = '0' * (2 - len(str(nxt_h))) + str(nxt_h)
            return nxt_h + ':' + min_v
        else:
            return min_v + ':' + min_v

    # previous closest time
    # hour = int(time[:2])
    # minute = int(time[3:])
    # nums = [int(time[0]), int(time[1]), int(time[3]), int(time[4])]

    # pre_h, pre_m = -1, -1
    # max_h, max_m = -1, -1

    # for i in range(4):
    #     for j in range(4):
    #         a = nums[i] * 10 + nums[j]
    #         if a < minute: 
    #             pre_m = max(pre_m, a)
    #         if a < hour:
    #             pre_h = max(pre_h, a)
    #         if a < 24:
    #             max_h = max(max_h, a)
    #         if a < 60:
    #             max_m = max(max_m, a)

    # max_h = '0' * (2 - len(str(max_h))) + str(max_h)
    # max_m = '0' * (2 - len(str(max_m))) + str(max_m)

    # if 0 <= pre_m < minute:
    #     return time[:3] + '0' * (2 - len(str(pre_m))) + str(pre_m)
    # elif 0 <= pre_h < hour:
    #     return '0' * (2 - len(str(pre_h))) + str(pre_h) + ':' + max_m
    # else:
    #     return max_h + ':' + max_m    