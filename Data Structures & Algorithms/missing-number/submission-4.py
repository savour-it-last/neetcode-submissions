class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        target_sum = n*(n-1)//2
        actual_sum = sum(nums)
        return target_sum - actual_sum
        