# problem #64

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                s1 = s2 = float('inf')
                if i - 1 >= 0:
                    s1 = grid[i - 1][j]
                if j - 1 >= 0:
                    s2 = grid[i][j - 1]
                    
                if s1 == float('inf') and s2 == float('inf'): 
                    continue 
                grid[i][j] += min(s1, s2)
                
        return grid[-1][-1]