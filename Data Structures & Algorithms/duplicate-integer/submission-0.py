class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        total = len(nums)
        for i,n in enumerate(nums):
            if n in nums[:i] + nums[i+1:]:
                return True
        return False