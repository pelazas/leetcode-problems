class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int total_gas = 0;
        int total_cost = 0;
        int current_tank = 0;
        int start_station = 0;

        for (int i = 0; i< gas.length; i++){
            total_gas += gas[i];
            total_cost += cost[i];
            current_tank += gas[i] - cost[i];

            if (current_tank <0){
                //start_station is invalid
                //any station between start_station and i is invalid
                start_station = i+1;
                current_tank = 0;
            }

        }
        if (total_gas < total_cost){ return -1; }
        return start_station;


    }
}