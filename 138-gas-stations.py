class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        total_tank = 0
        current_tank = 0
        station_start = 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            current_tank += gas[i] - cost[i]

            if current_tank < 0:
                station_start = i+1
                current_tank = 0

        if total_tank < 0:
            return -1
        else:
            return station_start
