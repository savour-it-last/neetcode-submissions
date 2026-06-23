class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # XOR solution. x ^ x is 0. So an array with all the nums and the actual range if xored together would leave out the last value
        nums.extend([i for i in range(len(nums)+1)])
        res = nums[0]
        for i in range(1, len(nums)):
            res^=nums[i]
        return res