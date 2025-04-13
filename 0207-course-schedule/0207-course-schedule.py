class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # time: (V+E), space: O(V)
        pre= prerequisites
        g= defaultdict(list)
        for a,b in pre:
            g[a].append(b)

        visiting=set()
        visited=set()

        def dfs(node):
            if node in visited:
                return True
            if node in visiting:
                return False
            visiting.add(node)

            for nei in g[node]:
                if not dfs(nei):
                    return False
            visiting.remove(node)
            visited.add(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        