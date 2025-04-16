class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        res=[]
        rows, cols= len(matrix), len(matrix[0])
        up, down= 0, rows-1
        left, right= 0, cols-1

        while len(res) < rows*cols:
            #traverse left to right
            for col in range(left, right+1):
                res.append(matrix[up][col])
            up+=1
            # top to bottom
            for row in range(up, down+1):
                res.append(matrix[row][right])
            right-=1

            #traverse right to left
            if up<= down:
                for col in range(right, left-1, -1):
                    res.append(matrix[down][col])
                down-=1

            #traverse bottom to up
            if left<= right:
                for row in range(down, up-1, -1):
                    res.append(matrix[row][left])
                left+=1
        return res