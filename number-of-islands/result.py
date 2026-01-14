class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # RECURSIVE DFS
        # def dfs(x,y):
        #     if x<0 or y<0 or x>len(grid)-1 or y > len(grid[0])-1: return
        #     if grid[x][y] == '0': return
        #     grid[x][y] = '0'
        #     dfs(x, y-1)
        #     dfs(x-1, y)
        #     dfs(x+1, y)
        #     dfs(x, y+1)

        # n_islands = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == '1':
        #             n_islands+=1
        #             dfs(i,j)

        # print(grid)
        # return n_islands

        # ITERATIVE BFS
        n_islands = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    n_islands+=1
                    queue = deque()
                    queue.append((i,j))
                    grid[i][j] = '0'

                    while queue:
                        curr_r, curr_c = queue.popleft()

                        #check left -> out of bounds and value 1
                        if curr_c -1 >= 0 and grid[curr_r][curr_c-1] == '1':
                            grid[curr_r][curr_c-1] = 0
                            queue.append((curr_r, curr_c-1))
                        #check right
                        if curr_c +1 < cols and grid[curr_r][curr_c+1] == '1':
                            grid[curr_r][curr_c+1] = 0
                            queue.append((curr_r, curr_c+1))
                        #check up
                        if curr_r -1 >= 0 and grid[curr_r-1][curr_c] == '1':
                            grid[curr_r-1][curr_c] = 0
                            queue.append((curr_r-1, curr_c))
                        #check down
                        if curr_r +1 < rows and grid[curr_r+1][curr_c] == '1':
                            grid[curr_r+1][curr_c] = 0
                            queue.append((curr_r+1, curr_c))
        return n_islands