class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        
        for w in words:
            temp = w.lower()
            flag = 1
            line = self.find_character(temp[0])
            for ltr in temp:
                if self.find_character(ltr) != line:
                    flag = 0
                    break;
            if flag == 1:
                ans.append(w)
        
        return ans
    
    def find_character(self, c):
        l1 = ['q','w','e','r','t','y','u','i','o','p']
        l2 = ['a','s','d','f','g','h','j','k','l']
        l3 = ['z','x','c','v','b','n','m']
        for l in l1:
            if l == c:
                return 1
        for l in l2:
            if l == c:
                return 2
        for l in l3:
            if l == c:
                return 3
        return -1
