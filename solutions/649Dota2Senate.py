class Solution:
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        r_re, d_re = 0, 0
        r_ban, d_ban = 0, 0
        
        win = False
        winner = ''
        
        senators = list(senate)
        
        while not win:
            r_re, d_re = 0, 0
            next_senators = []
            for i in range(len(senators)):
                if senators[i] == 'R':
                    if d_ban > 0:
                        d_ban -= 1
                    else:
                        r_ban += 1
                        r_re += 1
                        next_senators.append('R')
                else:
                    if r_ban > 0:
                        r_ban -= 1
                    else:
                        d_ban += 1
                        d_re += 1
                        next_senators.append('D')
            if r_re == 0 and d_re > 0:
                win = True
                winner = 'D'
            if d_re == 0 and r_re > 0:
                win = True
                winner = 'R'
            senators = next_senators
        
        if winner == 'R':
            return 'Radiant'
        else:
            return 'Dire'