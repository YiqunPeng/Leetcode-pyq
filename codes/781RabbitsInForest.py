class Solution:
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        max_color, color = [], []
        
        for answer in answers:
            if answer + 1 not in max_color:
                max_color.append(answer + 1)
                color.append(1)
                continue
            flag = 0
            for i in range(len(color)):
                if answer + 1 == max_color[i] and color[i] < max_color[i]:
                    flag = 1
                    color[i] += 1
                    break
            if flag == 0:
                max_color.append(answer + 1)
                color.append(1)
        
        # print(max_color)
        # print(color)
        return sum(max_color)
                
                