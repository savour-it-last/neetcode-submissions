class Solution:
    def propogate(self, nums: list[int], subset: list[int], start_index: int)->None:
        self.res.append(subset.copy())
        if start_index == len(nums):
            return None
        for curr_ind in range(start_index, len(nums)):
            if start_index < curr_ind and nums[curr_ind] == nums[curr_ind-1]:
                continue
            subset.append(nums[curr_ind])
            self.propogate(nums=nums, subset=subset, start_index=curr_ind+1)
            subset.pop(-1)

            

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res: list[list[int]] = []
        nums.sort()
        self.propogate(nums=nums, subset=[], start_index=0)
        return self.res