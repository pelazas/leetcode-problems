class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [-float('inf')] * len(nums)
        max_value = -float('inf')
        for i in range(len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            max_value = max(max_value, dp[i])
        return max_value
        