class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # For each index, I should store how many jumps it would take to reach target
        # when jumps match, they become a fleet.
        unobstructured_arrivals = []

        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        stack = []
        ind = 0
        fleets = 0
        while ind < len(cars):
            dist = target - cars[ind][0]
            arrival_time = dist/cars[ind][1]
            if not stack or stack[-1]<arrival_time:
                fleets+=1
                stack.append(arrival_time)
            ind+=1
        return fleets


        
