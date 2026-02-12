class Solution {
    public int maxArea(int[] height) {
        int l = 0;
        int r = height.length -1;
        int best_area = 0;
        
        while(l < r){
            int curr_area = Math.min(height[l], height[r]) * (r-l);
            best_area = Math.max(curr_area, best_area);
            if (height[r] > height[l]){
                l++;
            }else{
                r--;
            }
        }
        return best_area;
    }
}