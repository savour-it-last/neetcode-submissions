class Solution:
    def step(self, cost: list[int], index: int)->int:
        if index < 0:
            #basically this is when you start at 1 index
            # so nothing to add ig
            return 0
        if index == 0:
            return cost[0]

        if index in self.memory:
            return self.memory[index]
        
        one_step = self.step(cost=cost, index=index-1)
        two_step = self.step(cost=cost, index = index - 2) 
        min_step = min(one_step, two_step)
        if index < len(cost):
            min_step += cost[index]
        self.memory[index] = min_step
        return min_step

        
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.memory = {}
        return self.step(cost=cost, index = len(cost))

        