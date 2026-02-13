class Solution {
    public int orangesRotting(int[][] grid) {
        //bfs
        Queue<int[]> queue = new LinkedList<>(); //[row,col]
        int fresh_oranges = 0;

        // fill the queue initially
        for (int r = 0; r<grid.length; r++){
            for (int c = 0; c<grid[0].length; c++){
                if(grid[r][c] == 2){
                    queue.add(new int[]{r,c});
                }else if(grid[r][c] == 1){
                    fresh_oranges++;
                }
            }
        }
        if (fresh_oranges == 0) return 0;
        int minutes = 0;
        int[][] directions = {{1,0},{-1,0},{0,1},{0,-1}};

        while (!queue.isEmpty() && fresh_oranges >0){
            minutes++;
            int size = queue.size();

            for (int i = 0; i< size; i++){
                int[] current_coord = queue.poll();
                int r = current_coord[0];
                int c = current_coord[1];
                
                for (int[] d: directions){
                    int new_r = r+d[0];
                    int new_c = c+d[1];
                    // check out of bounds
                    if (new_r>= 0 && new_r <= (grid.length-1) && new_c>=0 && 
                    new_c <= (grid[0].length-1) && grid[new_r][new_c] == 1){
                        grid[new_r][new_c] = 2;
                        fresh_oranges--;
                        queue.add(new int[]{new_r,new_c});
                    }
                }
            }
        }
        return fresh_oranges == 0? minutes:-1;
    }
}