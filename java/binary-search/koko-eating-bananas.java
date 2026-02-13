class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int l = 1; 
        int r = 1;
        for (int pile : piles) {
            r = Math.max(r, pile);
        }
        
        int best_speed = r;

        while (r >= l){
            int mid = l+ (r-l)/2; // current eating speed
            long hours = 0;
            for (int pile: piles){
                hours += (pile + mid - 1) / mid;
            }
            if (hours > h){
                l = mid + 1;
            }else {
                best_speed = mid;
                r = mid-1;
            }
        }

        return best_speed;
    }
}