class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g= defaultdict(list)
        for a, b in prerequisites:
            g[a].append(b)
        order=[]
        visiting=set()
        visited=set()
        
        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            visiting.add(node)

            for nei in g[node]:
                if not dfs(nei):
                    return False
            
            visiting.remove(node)
            visited.add(node)
            order.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return order
        