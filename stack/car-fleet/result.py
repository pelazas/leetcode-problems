class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        paired_cars = zip(position, speed)
        cars = list(paired_cars)
        cars.sort() 
        cars.reverse() 

        fleets = 0
        max_time = 0

        for p,s in cars:
            time_to_reach = (target-p) / s

            if time_to_reach > max_time:
                fleets +=1
                max_time = time_to_reach
        
        return fleets