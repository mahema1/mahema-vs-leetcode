class Solution:
    def rob(self, nums: List[int]) -> int:
        n= len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0], nums[1])
        def robHouse(houses):
            m=len(houses)
            if m==1:
                return houses[0]
            if m==2:
                return max(houses[0], houses[1])
            dp=[0]*m
            dp[0]=houses[0]
            dp[1]= max(houses[0], houses[1])
            for i in range(2, m):
                dp[i] = max(houses[i] + dp[i-2], dp[i-1])
            return dp[-1]
        return max(robHouse(nums[1:]), robHouse(nums[:-1]))


        