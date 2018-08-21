# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    # dfs
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]   
        
        visited = set()
        visited.add((0, 0))
        robot.clean()

        def go_back():
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def dfs(i, j, d):
            for k in range(4):
                n_i, n_j = i + directions[d][0], j + directions[d][1]
                if (n_i, n_j) not in visited and robot.move():
                    visited.add((n_i, n_j))
                    robot.clean()
                    dfs(n_i, n_j, d)
                    go_back()
                    
                robot.turnRight()
                d = (d + 1) % 4
                                        
        dfs(0, 0, 0)       