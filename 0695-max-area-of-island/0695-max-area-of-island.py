class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols= len(grid), len(grid[0])
        visit=set()

        def dfs(r,c):
            if (r<0 or c<0 or r>= rows or c>= cols or grid[r][c]!=1 or (r,c) in visit):
                return 0
            visit.add((r,c))
            return 1+ dfs(r+1, c)+dfs(r-1, c)+ dfs(r,c+1)+ dfs(r, c-1)
        maxarea=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]== 1 and (r,c) not in visit:
                    area= dfs(r,c)
                    maxarea= max(area, maxarea)        
        return maxarea