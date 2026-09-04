class Solution:
    def make_jump(self, nums: list[int], curr_ind: int) -> int:
        if curr_ind >= len(nums) - 1:
            return 0

        if curr_ind in self.mem:
            return self.mem[curr_ind]

        max_jump = curr_ind + nums[curr_ind]
        min_jump = len(nums)

        for jump in range(max_jump, curr_ind, -1):
            new_ind = jump
            jumps = 1 + self.make_jump(
                nums=nums,
                curr_ind=new_ind,
            )
            min_jump = min(min_jump, jumps)

        self.mem[curr_ind] = min_jump
        return min_jump

    def jump(self, nums: list[int]) -> int:
        self.mem = {}
        return self.make_jump(nums=nums, curr_ind=0)