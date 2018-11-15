class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digit, letter = [], []
        for log in logs:
            if log[-1] in '0123456789':
                digit.append(log)
            else:
                letter.append(log)
        
        parts = [l.split(' ', 1) for l in letter]        
        parts.sort(key=lambda x:(x[1], x[0]))
    
        return [p[0] + ' ' + p[1] for p in parts] + digit  