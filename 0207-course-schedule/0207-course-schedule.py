class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre= prerequisites
        g= defaultdict(list)
        for a,b in pre:
            g[a].append(b)
        
        unvisited= 0
        visiting=set()
        visited=set()
        # states=[unvisited] * numCourses 

        def dfs(node):
            # state= states[node]
            if node in visited: return True

            if node in visiting: return False

            visiting.add(node)

            for nei in g[node]:
                if not dfs(nei):
                    return False
            visited.add(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
        