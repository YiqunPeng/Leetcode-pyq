class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        def list2dic(l, d_n, d_c):
            for i in xrange(len(l)):
                if d_n.has_key(l[i]):
                    d_n[l[i]] += i
                    d_c[l[i]] += 1
                else:
                    d_n[l[i]] = i
                    d_c[l[i]] = 1
            
        ans = []
        dict_name = {}
        dict_cnt = {}
        list2dic(list1, dict_name, dict_cnt)
        list2dic(list2, dict_name, dict_cnt)
        min_index = sys.maxsize
        for key in dict_cnt:
            if dict_name[key] < min_index and dict_cnt[key] == 2:
                min_index = dict_name[key]
        for key in dict_cnt:
            if dict_name[key] == min_index and dict_cnt[key] == 2:
                ans += [key]
        return ans
        