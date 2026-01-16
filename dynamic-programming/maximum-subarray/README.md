DIFFICULTY: MEDIUM

Dynamic Programming approach.
`dp[i]` stores the maximum sum of a subarray ending at index `i`.

The recurrence relation is:
`dp[i] = max(dp[i-1] + nums[i], nums[i])`

This means the max subarray ending at `i` is either the current number or the current number added to the max subarray ending at `i-1`.

The final result is the maximum value in the `dp` array.
