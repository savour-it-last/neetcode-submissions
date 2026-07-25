# Definition for completeness
# class Solution:

class Solution:
    def step(self, cost: list[int], index: int) -> int:
        """
        Returns the minimum cost to stand on stair 'index'.
        """
        if index <= 1:
            return cost[index]

        if self.memory[index] > -1:
            return self.memory[index]

        one_step = self.step(cost=cost, index=index - 1)
        two_step = self.step(cost=cost, index=index - 2)

        min_step = cost[index] + min(one_step, two_step)

        self.memory[index] = min_step
        return min_step

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost)

        self.memory = [-1] * len(cost)

        return min(
            self.step(cost=cost, index=len(cost) - 1),
            self.step(cost=cost, index=len(cost) - 2),
        )