CONTAINS NEARBY DUPLICATE II - Difficulty: EASY

The logic here is that based on this constraint ```abs(i - j) <= k```, we have a window of exactly size k+1 - SLIDING WINDOW. 

As the array is unordered, is best to use a set or dictionary to keep track of previous numbers to find duplicates

COMPLEXITY:
- time: O(N)
- space: O(k) -> the set will be as long as k