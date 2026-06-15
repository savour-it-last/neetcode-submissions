class Solution:
    def solution(self, index: int,nums: list[int], target: int, curr: list[int]) -> None:
        if target<0 or index == len(nums):
            return None
        if target == 0:
            self.result.append(curr.copy())
            return None
        value = nums[index]
        #exclude current
        self.solution(index=index+1, nums=nums, target=target, curr=curr)
        curr.append(value)
        target -= value
        # include current
        self.solution(index=index, nums=nums, target=target, curr=curr)
        curr.pop()

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
       self.result = [] 
       self.solution(index=0, nums=nums, target=target, curr=[])
       return list(self.result)