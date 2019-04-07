class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        right = (1,0)
        down = (0,-1)
        left = (-1,0)
        up = (0,1)     
        coord = {
            right: 'right',
            down: 'down',
            left: 'left',
            up: 'up'
        }
        # We'll be turning right
        directions = {
            'right': [right,down,left,up],
            'down': [down,left,up,right],
            'left': [left,up,right,down],
            'up': [up,right,down,left]
        }
        visited = set()
        
        def dfs(x,y,facing):
            robot.clean()
            visited.add((x,y))
            for way in directions[facing]:
                movex, movey = way
                nextx = x + movex
                nexty = y + movey
                if (nextx,nexty) not in visited and robot.move():
                    facing = coord[(movex,movey)]
                    dfs(nextx,nexty,facing)
		    # Put robot back to where it started before dfs call 
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()
                robot.turnRight() # Turn right to follow directions
        dfs(0,0,'up')
