class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        gn = []
        gt = []
        
        pre = ''
        cnt = 0
        for i in range(len(name)):
            if not pre:
                pre = name[i]
                cnt = 1
            else:
                if name[i] != pre:
                    gn.append((pre, cnt))
                    pre = name[i]
                    cnt = 1
                else:
                    cnt += 1
        gn.append((pre, cnt))
        
        pre = ''
        cnt = 0
        for i in range(len(typed)):
            if not pre:
                pre = typed[i]
                cnt = 1
            else:
                if typed[i] != pre:
                    gt.append((pre, cnt))
                    pre = typed[i]
                    cnt = 1
                else:
                    cnt += 1
        gt.append((pre, cnt))
        
        if len(gn) != len(gt): return False
        
        for i in range(len(gn)):
            if gn[i][0] != gt[i][0]:
                return False
            if gn[i][1] > gt[i][1]:
                return False
        return True