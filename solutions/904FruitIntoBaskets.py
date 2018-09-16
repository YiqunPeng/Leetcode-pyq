class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        a, b = 1, 0
        ta, tb = tree[0], -1
        
        ans = 0
        
        for i in range(1, len(tree)):
            if ta == tree[i]:
                a += 1
                continue
            elif tb == tree[i]:
                b += 1
                continue
            else:
                if tb == -1:
                    b = 1
                    tb = tree[i]
                else:
                    ans = max(a + b, ans)
                    nb = 1
                    ntb = tree[i-1]
                    pos = i - 2
                    while pos and tree[pos] == tree[pos+1]:
                        nb += 1
                        pos -= 1
                    ta = tree[i]
                    tb = ntb
                    a = 1
                    b = nb

        return max(ans, a + b)