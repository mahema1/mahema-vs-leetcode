class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #1. Capture all the O -> T which are at the border.- DFS
        #2. Caputre everything on the board which are X or O-> X
        #3. Capture the T-> O
        rows, cols= len(board), len(board[0])
        def dfs(r, c):
            if (r<0 or c<0 or r>= rows or c>= cols or board[r][c]!='O'):
                return 
            board[r][c]="T"
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1,c)
            dfs(r,c-1)
        #mark O-T on the border
        for r in range(rows):
            for c in range(cols):
                if (board[r][c]=="O" and( r in[0, rows-1] or c in [0, cols-1])):
                    dfs(r,c)
        #mark all as X
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"

        #mark all T-> O            
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="T":
                    board[r][c]="O"