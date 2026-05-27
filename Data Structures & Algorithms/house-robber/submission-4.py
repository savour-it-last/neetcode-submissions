class Solution:
    def best_sum(self, nums: List[int], curr_index: int) -> int:
        if curr_index in self.memory:
            return self.memory[curr_index]
        best_current = max(
            self.best_sum(nums=nums, curr_index=curr_index - 1),
            self.best_sum(nums=nums, curr_index=curr_index - 2) + nums[curr_index],
        )
        self.memory[curr_index] = best_current
        return best_current

    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums)

        self.memory = {0: nums[0], 1: max(nums[0], nums[1])}

        return self.best_sum(nums=nums, curr_index=len(nums) - 1)
