class Solution:
    def recursive_subset(self, nums: list[int], index: int, subset: list[int])->None:
        if index == len(nums):
            self.res.append(subset)
            return None
        inclusive_subset = subset + [nums[index]]
        included = self.recursive_subset(nums=nums, index=index+1, subset=inclusive_subset)
        excluded = self.recursive_subset(nums=nums, index=index+1, subset=subset)
        

         
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.recursive_subset(nums=nums, index=0, subset=[])
        return self.res