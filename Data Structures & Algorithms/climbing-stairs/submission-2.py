class Solution:
    def step(self, step: int) -> int:
        if step in self.memory:
            return self.memory[step]
        if step == 1:
            return 1
        if step == 2:
            return 2
        
        step_result =  self.step(step=step-1) + self.step(step=step-2)
        self.memory[step] = step_result
        return step_result

    def climbStairs(self, n: int) -> int:
        self.memory = {}
        return self.step(step=n)
