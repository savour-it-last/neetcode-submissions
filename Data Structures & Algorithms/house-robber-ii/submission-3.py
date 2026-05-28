class Solution:
    def best_amount(self, nums: List[int], curr_index: int) -> int:
        if curr_index in self.memory:
            return self.memory[curr_index]
        curr_best = max(
            self.best_amount(nums=nums, curr_index=curr_index - 1),
            self.best_amount(nums=nums, curr_index=curr_index - 2) + nums[curr_index],
        )
        self.memory[curr_index] = curr_best
        return curr_best

    def solve_linear(self, nums: list[int])->int:
        if len(nums) < 3:
            return max(nums)
        self.memory = {0: nums[0], 1: max(nums[0], nums[1])}
        last_index = len(nums) - 1
        return self.best_amount(nums=nums, curr_index=last_index)

    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        last_index = len(nums) - 1
        best = max(
            self.solve_linear(nums=nums[1:]),
            self.solve_linear(nums=nums[:last_index]),
        )
        return best
