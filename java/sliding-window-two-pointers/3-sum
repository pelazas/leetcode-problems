class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums); // O(nlogn)

        HashSet<List<Integer>> set = new HashSet<>();
        int l;
        int r;

        for (int i = 0; i < nums.length -2; i++){
            l = i+1;
            r = nums.length -1;
            // skip duplicates
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            while (l < r){
                int operation = nums[i] + nums[l] + nums[r];
                if (operation == 0){
                    set.add(Arrays.asList(nums[i], nums[l], nums[r]));
                    l++;
                } else if (operation > 0){
                    r--;
                } else{
                    l++;
                }
            }
        }
        return new ArrayList(set);
        // convert set to list

        
    }
}