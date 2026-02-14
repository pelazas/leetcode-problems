class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # binary search + bfs?
        def canReach(t):
            if grid[0][0] > t:
                return False
            queue = deque([(0, 0)])
            visited = set([(0, 0)])
            directions = [(1,0),(-1,0),(0,1),(0,-1)]

            while queue:
                r,c = queue.popleft()
                
                if r == len(grid)-1 and c == len(grid[0])-1:
                    return True

                for dr, dc in directions:
                    new_r, new_c = r+dr, c+dc

                    if 0 <= new_r <= len(grid)-1 and 0 <= new_c <= len(grid[0])-1:
                        if (new_r, new_c) not in visited and grid[new_r][new_c] <= t:
                            visited.add((new_r, new_c))
                            queue.append((new_r, new_c))

            return False


        max_val = max(max(row) for row in grid)

        best_t = max_val
        l = 0
        r = max_val
        while r>=l:
            mid = l + (r-l) // 2
            if canReach(mid):
                best_t = mid
                r = mid -1
            else:
                #t is higher (right half)
                l = mid+1
        return best_t
        
        
        