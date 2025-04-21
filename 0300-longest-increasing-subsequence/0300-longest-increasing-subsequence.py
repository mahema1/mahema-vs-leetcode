class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Edge case: if array is empty, return 0
        if not nums:
            return 0

        # Initialize DP array where dp[i] is the length of LIS ending at index i
        dp = [1] * len(nums)

        # Iterate through each number in the array
        for i in range(len(nums)):
            # Check all previous elements to find smaller numbers
            for j in range(i):
                if nums[j] < nums[i]:
                    # If we found a smaller element, try updating dp[i]
                    dp[i] = max(dp[i], dp[j] + 1)

        # The result is the maximum value in the DP array
        return max(dp)
