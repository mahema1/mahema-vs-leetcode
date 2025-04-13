class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # if not grid:
        #     return 0
        # visited= set()
        # islands=0
        # rows, cols= len(grid), len(grid[0])
        # def bfs(r, c):
        #     q= deque()
        #     visited.add((r,c))
        #     q.append((r,c))
        #     while q:
        #         row, col= q.popleft()
        #         directions=[[1,0], [0,1], [0,-1], [-1,0]]
        #         for dr, dc in directions:
        #             r, c= row+dr, col+dc
        #             if r in range(rows) and c in range(cols) and (r,c) not in visited and grid[r][c]=="1":
        #                 q.append((r,c))
        #                 visited.add((r,c))



        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c]=="1" and (r,c) not in visited:
        #             bfs(r, c)
        #             islands+=1
        # return islands
        
        if not grid:
            return 0
        visit=set()
        rows, cols= len(grid), len(grid[0])
        island=0

        def dfs(r,c):
            if (r<0 or c<0 or r>=rows or c>=cols or grid[r][c]!='1' or (r,c) in visit):
                return 
            visit.add((r,c))
            directions= [[1,0], [-1,0], [0,1], [0,-1]]
            for dr, dc in directions:
                dfs(r+dr,c+dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1' and (r,c) not in visit:
                    dfs(r,c)
                    island+=1
        
        return island