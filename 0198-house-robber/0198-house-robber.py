class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1, rob2= 0, 0 #rob2 before, rob1 the one before that 
        # #[rob1, rob2, n, n+1, ....]
        # for n in nums:
        #     temp= max(n+rob1, rob2)
        #     rob1= rob2
        #     rob2= temp
        # return rob2

        n= len(nums)
        
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0], nums[1])

        dp=[0]*n
        dp[0]= nums[0]
        dp[1]= max(nums[0], nums[1])
        for i in range(2, n):
            dp[i]= max(nums[i]+dp[i-2], dp[i-1])
        return dp[n-1]
         
        