class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh_orange = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    queue.append((r,c,0))
                if grid[r][c] == 1:
                    fresh_orange +=1

        minutes_passed = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            r,c,t = queue.popleft()
            minutes_passed = t
            for dr, dc in directions:
                if 0 <= r+dr < len(grid) and 0 <= c+dc < len(grid[0]) and grid[r+dr][c+dc] == 1:
                    grid[r+dr][c+dc] = 2
                    fresh_orange -=1
                    queue.append((r+dr, c+dc, t+1))

        return minutes_passed if fresh_orange == 0 else -1



        