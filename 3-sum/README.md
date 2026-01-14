3 SUM - DIFFICULTY: MEDIUM

This problem can be done like the 2 sum with an extra loop. (first solution)

For principal solution
- Sort array: Important to enable 2 pointer strategy
- Iterate through array to fix first number (nums[i])
- Two pointers: left and right to find the other numbers to sum

Key takeaways
- If output must not contain duplicates-> sorting + sets
- movement: sum too low? move left pointer to the right, sum too high? move right pointer to the left

Complexity:
- Time O(N2)
- Space O(N) (found_triplets array)