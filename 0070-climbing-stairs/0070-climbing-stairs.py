class Solution:
    def climbStairs(self, n: int) -> int:

        #time: O(n), space:O(n)
        if n==1:
            return 1
        if n==2:
            return 2
        dp=[0]*n
        dp[0]=1
        dp[1]=2
        for i in range(2, n):
            dp[i]= dp[i-2]+dp[i-1]

        return dp[n-1]

        # #time: O(n), space: O(1)
        # if n==1:
        #     return 1
        # if n==2:
        #     return 2
        # prev=1
        # cur=2
        # for i in range(2, n):
        #     prev, cur= cur, prev+cur
        # return cur