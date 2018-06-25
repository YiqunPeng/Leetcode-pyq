class Solution:
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        val, coe = 0, 0
        mode = 1
        
        pos = 0
        v, sign = '', 1
        while pos < len(equation):
            if equation[pos] == 'x':
                if v == '': v = '1'
                coe += sign * int(v) * mode
                v, sign = '', 1
            elif equation[pos] == '+':
                if v == '': v = '0'
                val += int(v) * sign * -mode
                v, sign = '', 1
            elif equation[pos] == '-':
                if v == '': v = '0'
                val += int(v) * sign * -mode
                v, sign = '', -1
            elif equation[pos] == '=':
                if v == '': v = '0'
                val += int(v) * sign * -mode
                v, sign = '', 1
                mode = -1
            else:
                v = v + equation[pos]
            pos += 1
        if v != '':
            val += int(v) * sign

        if coe == 0:
            if val == 0:
                return 'Infinite solutions'
            else:
                return 'No solution'
        else:
            return 'x=' + str(val // coe)
        

                