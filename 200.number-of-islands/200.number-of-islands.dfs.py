class Solution:
    def numIslands(self, grid: 'List[List[str]]') -> 'int':
        lx = len(grid)
        if lx == 0: return 0
        ly = len(grid[0])
        if ly == 0: return 0
        count = 0
        
        def dfs(x,y):
            grid[x][y] = '0'
            if x+1 < lx and grid[x+1][y] == '1': dfs(x+1,y)
            if x-1 >= 0 and grid[x-1][y] == '1': dfs(x-1,y)
            if y+1 < ly and grid[x][y+1] == '1': dfs(x, y+1)
            if y-1 >= 0 and grid[x][y-1] == '1': dfs(x, y-1)
                
        for x in range(0,lx):
            for y in range(0,ly):
                if grid[x][y] == '1':
                    count += 1
                    dfs(x,y)
        return count
