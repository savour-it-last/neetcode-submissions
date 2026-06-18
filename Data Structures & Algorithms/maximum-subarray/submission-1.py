class Solution:
    def solution(self, index: int, nums: list[int], prev_max: int) -> None:
        if index == len(nums):
            return None
        curr_sum = nums[index] + prev_max
        curr_max = max(nums[index], prev_max + nums[index])
        self.max_sum = max(self.max_sum, curr_max)
        self.solution(index=index+1, nums=nums, prev_max=curr_max)
        return None
            

    def maxSubArray(self, nums: List[int]) -> int:
        self.max_sum = nums[0]
        self.solution(index=1, nums=nums, prev_max=nums[0])
        return self.max_sum



        