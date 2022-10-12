class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ret = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1':
                    self.dfs(row, col, grid)
                    ret += 1
                    
        return ret
    
    def dfs(self, row, col, grid):
        grid[row][col] = '0'
        
        for i in range(4):
            cr = row
            cc = col
            
            if i == 0 and row > 0:
                cr -= 1
            elif i == 1 and row < len(grid) - 1:
                cr += 1
            elif i == 2 and col > 0:
                cc -= 1
            elif i == 3 and col < len(grid[0]) - 1:
                cc += 1 
                
            if grid[cr][cc] == '1':
                self.dfs(cr, cc, grid)
                
