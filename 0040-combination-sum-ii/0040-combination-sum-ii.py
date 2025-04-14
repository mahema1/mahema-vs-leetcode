class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort(key= lambda x: x)
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return 
            if total > target or i>= len(candidates):
                return 
            
            # include the i 
            cur.append(candidates[i])
            dfs(i+1, cur, total+candidates[i]) # i+1- we do not reuse the index i
            # do not include the i
            cur.pop()
            while i+1< len(candidates) and candidates[i]== candidates[i+1]:
                i+=1
            dfs(i+1, cur, total)

        dfs(0, [], 0)
        return res
        