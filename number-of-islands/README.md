NUMBER OF ISLANDS - DIFFICULTY: MEDIUM

The idea is to find an island, expand on it either bfs or dfs until done, set all the '1s' to '0s' update the number of islands and keep iterating until done.


Depth-first Search - Recursive
On every '1' found, update n_islands, expand up, right, down, left recursively to remove adjacent '1s'.

Breadth-first Search - Iterative
Instead of recursion use a FIFO queue, where on a found island expand it up,right, down, left to the queue
