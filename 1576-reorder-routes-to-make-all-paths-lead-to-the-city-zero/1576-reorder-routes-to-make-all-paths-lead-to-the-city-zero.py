class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges= set() # for constant look up, the array above takes O(n) look up time but set O(1)
        neighbours= defaultdict(list)
        for a,b in connections:
            edges.add((a,b))
            neighbours[a].append(b)
            neighbours[b].append(a)
        change=0
        visit= set()


        def dfs(city):
            nonlocal change
            if city in visit:
                return 
            visit.add(city)
            for nei in neighbours[city]:
                if nei in visit:
                    continue
                if (nei, city) not in edges:
                    change+=1
                dfs(nei)
        dfs(0)
        return change




        