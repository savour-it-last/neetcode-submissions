class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = max(nums)
        curr_max = 1
        curr_min = 1
        for num in nums:
            val_1 = curr_max * num
            val_2 = curr_min * num
            curr_max = max(val_1, val_2, num)
            curr_min = min(val_1, val_2, num)
            max_prod = max(max_prod, curr_max)

        return max_prod