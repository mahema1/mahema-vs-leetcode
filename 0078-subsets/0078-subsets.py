class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # for each number we have two choices- one to include it and second to not include it 
        res=[]

        subset=[] # each subset

        def dfs(i):#i- index 
            if i >=len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1) 

            #decision to not include nums[i]
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res


        