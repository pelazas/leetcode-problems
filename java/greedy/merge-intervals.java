class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

        List<int[]> result = new ArrayList<>();
        int[] current_interval = intervals[0];
        result.add(current_interval);

        for(int[] interval: intervals){
            int currentEnd = current_interval[1];
            int nextStart = interval[0];
            int nextEnd = interval[1];

            if (nextStart <= currentEnd){
                current_interval[1] = Math.max(currentEnd, nextEnd);
            }else{
                current_interval = interval;
                result.add(current_interval);
            }
        }
        return result.toArray(new int[result.size()][]);
    }
}