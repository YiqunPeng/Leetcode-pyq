class Solution:
    # string
    # time: O(n^2) n -- len(time)
    # space: O(n)
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

    # previous closet time, use each digit once
    # dfs
    # time: O(4^n)
    # space: O(4^n)    
    # def previousClosestTimeNoDuplicate(time):
    #     nums = [time[0], time[1], time[3], time[4]]
    #     res = []

    #     def dfs(curr, used):
    #         if len(curr) == 4:
    #             res.append(curr)
    #         for i in range(4):
    #             if i not in used:
    #                 used.add(i)
    #                 dfs(curr+nums[i], used)
    #                 used.remove(i)

    #     dfs('', set())
        
    #     pre_time = '-1'
    #     tm = time[:2] + time[3:]
    #     for t in res:
    #         if t < tm:
    #             hour = int(t[:2])
    #             minute = int(t[2:])
    #             if 0 <= hour < 24 and 0 <= minute < 60:
    #                 pre_time = max(pre_time, t, key=int)

    #     if pre_time != '-1': return pre_time[:2] + ':' + pre_time[2:]

    #     for t in res:
    #         hour = int(t[:2])
    #         minute = int(t[2:])
    #         if 0 <= hour < 24 and 0 <= minute <60:
    #             pre_time = max(pre_time, t, key=int)
    #     return pre_time[:2] + ':' + pre_time[2:]

    # next closet time, use each digit once
    # dfs
    # time: O(4^n)
    # space: O(4^n)
    # def nextClosestTimeNoDuplicates(self, time):
    #     nums = [time[0], time[1], time[3], time[4]]
    #     res = []

    #     def dfs(curr, used):
    #         if len(curr) == 4:
    #             res.append(curr)
    #         for i in range(4):
    #             if i not in used:
    #                 used.add(i)
    #                 dfs(curr+nums[i], used)
    #                 used.remove(i)

    #     dfs('', set())
        
    #     nxt_time = '9999'
    #     tm = time[:2] + time[3:]
    #     for t in res:
    #         if t > tm:
    #             hour = int(t[:2])
    #             minute = int(t[2:])
    #             if 0 <= hour < 24 and 0 <= minute < 60:
    #                 nxt_time = min(nxt_time, t, key=int)

    #     if nxt_time != '9999': return nxt_time[:2] + ':' + nxt_time[2:]

    #     for t in res:
    #         hour = int(t[:2])
    #         minute = int(t[2:])
    #         if 0 <= hour < 24 and 0 <= minute <60:
    #             nxt_time = min(nxt_time, t, key=int)
    #     return nxt_time[:2] + ':' + nxt_time[2:]

    # previous closest time
    # def previousClosestTime(self, time):
    #     hour = int(time[:2])
    #     minute = int(time[3:])
    #     nums = [int(time[0]), int(time[1]), int(time[3]), int(time[4])]

    #     pre_h, pre_m = -1, -1
    #     max_h, max_m = -1, -1

    #     for i in range(4):
    #         for j in range(4):
    #             a = nums[i] * 10 + nums[j]
    #             if a < minute: 
    #                 pre_m = max(pre_m, a)
    #             if a < hour:
    #                 pre_h = max(pre_h, a)
    #             if a < 24:
    #                 max_h = max(max_h, a)
    #             if a < 60:
    #                 max_m = max(max_m, a)

    #     max_h = '0' * (2 - len(str(max_h))) + str(max_h)
    #     max_m = '0' * (2 - len(str(max_m))) + str(max_m)

    #     if 0 <= pre_m < minute:
    #         return time[:3] + '0' * (2 - len(str(pre_m))) + str(pre_m)
    #     elif 0 <= pre_h < hour:
    #         return '0' * (2 - len(str(pre_h))) + str(pre_h) + ':' + max_m
    #     else:
    #         return max_h + ':' + max_m    