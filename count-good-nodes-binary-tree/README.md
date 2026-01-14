COUNT GOOD NODES IN BINARY TREE - difficulty: MEDIUM

Binary trees - DEPTH FIRST SEARCH

HOW TO IDENTIFY THE ALGORITHM
- "path from root": DFS allows you to follow single path from root to leaf carrying a state (max_val)

WHY PRE-ORDER DFS
- the children depend on the parents data (process max_val before calling dfs on leafs)

KEY TAKEAWAYS
- Let the function return only the count for its own subtree. Carefull with double counting

COMPLEXITY
- Time complexity: O(N)
- Space complexity: O(H) height of the tree. in the worst case this is O(N)