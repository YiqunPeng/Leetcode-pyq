class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        ans = 0
        
        obstacles = set([(i,j) for i,j in obstacles])
        
        # up, right, down, left
        fx = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr = 0
        x, y = 0, 0
        
        for cmd in commands:
            if cmd == -2:
                curr = (curr-1) % 4
            elif cmd == -1:
                curr = (curr+1) % 4
            elif 1 <= cmd <= 9:
                dx, dy = x+cmd*fx[curr][0], y+cmd*fx[curr][1]
                if curr == 1:
                    for i in range(x, dx+1):
                        if (i, dy) in obstacles:
                            dx = i - 1
                            break
                elif curr == 3:
                    for i in range(x, dx-1, -1):
                        if (i, dy) in obstacles:
                            dx = i + 1
                            break
                elif curr == 0:
                    for j in range(y, dy+1):
                        if (dx, j) in obstacles:
                            dy = j - 1
                            break
                elif curr == 2:
                    for j in range(y, dy-1, -1):
                        if (dx, j) in obstacles:
                            dy = j + 1
                            break
                x, y = dx, dy
                ans = max(ans, dx*dx+dy*dy)
        
        return ans