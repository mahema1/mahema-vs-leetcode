class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        res=0
        visit=set()
        def dfs(node, res):
            if node in visit:
                return 
            visit.add(node)
            res.append(node)
            for nei in adj[node]:
                dfs(nei, res)
            return res
        
        for i in range(n):
            if i in visit:
                continue
            component= dfs(i, [])
            flag= True
            for v in component:
                if len(component)-1 != len(adj[v]):
                    flag=False
                    break
            if flag:
                res+=1
        return res
        