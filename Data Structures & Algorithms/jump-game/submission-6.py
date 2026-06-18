class Solution:
    def solution(self, nums: list[int], index: int)->bool:
        if index in self.memory:
            return self.memory[index]
        if index>=len(nums)-1:
            self.memory[index] = True
            return True
        if nums[index]==0:
            self.memory[index] = False
            return False
        max_jump = nums[index]
        reach = False
        for jump in range(max_jump, 0, -1):
            if self.solution(nums=nums, index=index+jump):
                reach = True
                break
        self.memory[index] = reach
        return reach

    def canJump(self, nums: List[int]) -> bool:
        self.memory = {}
        return self.solution(nums=nums, index=0)