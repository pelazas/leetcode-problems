class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<>(); // remove duplicates
        // could do a sort, but O(nlogn)

        for (int num: nums){
            set.add(num);
        }

        int best_length = 0;

        for (int num : set){

            if (!set.contains(num - 1)) {
                int current_num = num;
                int current_len = 1;
                while (set.contains(current_num +1)){
                    current_num++;
                    current_len++;
                }
                best_length = Math.max(best_length, current_len);
            }
            
        }
        return best_length;
    }
}