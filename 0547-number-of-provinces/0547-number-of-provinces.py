class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(i):
            visited.add(i)
            for j in range(len(isConnected)):
                if isConnected[i][j] and j not in visited:
                    dfs(j)
            return 

        visited=set()
        province=0
        for i in range(len(isConnected)):
            if i not in visited:
                province+=1
                dfs(i)
        return province