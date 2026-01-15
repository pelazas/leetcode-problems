MINIMUM SIZE SUBARRAY SUM - DIFFICULTY: MEDIUM

- subarray: contiguous elements in the array (can't sort)
- ```counter + new_element >= target``` -> move window (l or r), expand right pointer, add to sum
- if sum < target -> shrink left pointer, update min_length.

COMPLEXITY:
- time: O(n) 
- space: O(1)

