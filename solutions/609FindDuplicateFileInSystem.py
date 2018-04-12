class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        
        for path in paths:
            splits = path.split(' ')
            dic_path = splits[0] + '/'
            for sp in splits[1:]:
                name = sp.split('(')[0]
                content = sp.split('(')[1][:-1]
                if dic.has_key(content):
                    dic[content].append(dic_path+name)
                else:
                    dic[content] = [dic_path+name]
        
        ans = []
        
        for keys in dic.keys():
            if len(dic[keys]) > 1:
                ans.append(dic[keys])
        
        return ans